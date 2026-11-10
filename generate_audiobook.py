import os
import sys
import glob
import re
import argparse
import numpy as np
import soundfile as sf

import static_ffmpeg
static_ffmpeg.add_paths()
from f5_tts.api import F5TTS

REF_AUDIO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ref_voice_first_sentence.wav")
REF_TEXT = "The air carries a chill, sharp enough to prick the skin beneath my sleeves."

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audiobook")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def split_text_into_chunks(text, max_chars=250):
    """
    Split text into natural speaking sentences/clauses under max_chars.
    """
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks = []
    
    for p in paragraphs:
        # Split on sentence boundaries
        sentences = re.split(r'(?<=[.!?])\s+', p)
        curr_chunk = ""
        for s in sentences:
            s = s.strip()
            if not s:
                continue
            if len(curr_chunk) + len(s) + 1 <= max_chars:
                curr_chunk = f"{curr_chunk} {s}".strip()
            else:
                if curr_chunk:
                    chunks.append((curr_chunk, False)) # False = sentence within paragraph
                curr_chunk = s
        if curr_chunk:
            chunks.append((curr_chunk, True)) # True = end of paragraph (longer pause)
            
    return chunks

def generate_chapter(f5, chapter_file, speed=0.85):
    base_name = os.path.splitext(os.path.basename(chapter_file))[0]
    with open(chapter_file, "r", encoding="utf-8") as f:
        content = f.read().strip()
    
    # Get title from first line
    lines = content.split("\n")
    title_line = lines[0].strip()
    safe_title = re.sub(r'[^a-zA-Z0-9_\- ]', '', title_line).replace(' ', '_')
    out_wav = os.path.join(OUTPUT_DIR, f"{safe_title}.wav")
    out_mp3 = os.path.join(OUTPUT_DIR, f"{safe_title}.mp3")
    
    print(f"\n=======================================================")
    print(f"Generating Audiobook: {title_line}")
    print(f"Output File: {out_wav}")
    print(f"=======================================================")
    
    chunks = split_text_into_chunks(content)
    print(f"Total spoken segments to synthesize: {len(chunks)}")
    
    audio_segments = []
    sr = 24000
    
    # Create pause buffers
    sentence_pause = np.zeros(int(sr * 0.25)) # 250ms
    paragraph_pause = np.zeros(int(sr * 0.55)) # 550ms
    
    for idx, (chunk_text, is_para_end) in enumerate(chunks):
        print(f"[{idx+1}/{len(chunks)}] {chunk_text[:60]}...")
        wav, sr, _ = f5.infer(
            ref_file=REF_AUDIO,
            ref_text=REF_TEXT,
            gen_text=chunk_text,
            speed=speed
        )
        audio_segments.append(wav)
        if is_para_end:
            audio_segments.append(paragraph_pause)
        else:
            audio_segments.append(sentence_pause)
            
    full_audio = np.concatenate(audio_segments)
    
    # Normalize to -1.0 dB
    peak = np.max(np.abs(full_audio))
    if peak > 0:
        full_audio = full_audio / peak * 0.89
        
    sf.write(out_wav, full_audio, sr)
    
    # Also convert to MP3 using ffmpeg
    ffmpeg_bin = r'C:\Users\ChristopherAllen\audiobook_env\Lib\site-packages\static_ffmpeg\bin\win32\ffmpeg.EXE'
    import subprocess
    subprocess.run([ffmpeg_bin, '-y', '-i', out_wav, '-codec:a', 'libmp3lame', '-b:a', '192k', out_mp3], capture_output=True)
    
    duration_sec = len(full_audio) / sr
    print(f"\n[DONE] Saved: {out_wav}")
    print(f"Duration: {duration_sec:.1f}s ({duration_sec/60:.2f} mins)")
    return out_wav

def main():
    parser = argparse.ArgumentParser(description="Generate audiobook of The Route in Christopher Allen's voice")
    parser.add_argument("--chapter", type=str, default="1", help="Chapter number (e.g. 1, 2) or 'all'")
    parser.add_argument("--speed", type=float, default=0.85, help="Speaking speed (between 0.75 and 1.0, default 0.85)")
    args = parser.parse_args()
    
    print(f"Initializing F5-TTS voice cloning engine on RTX 4070 GPU (Speed: {args.speed})...")
    f5 = F5TTS()
    print("Voice model loaded successfully!")
    
    ch_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chapters")
    
    if args.chapter.lower() == "all":
        ch_files = sorted(glob.glob(os.path.join(ch_dir, "chapter_*.txt")))
        print(f"Synthesizing all {len(ch_files)} chapters at speed {args.speed}...")
        for cf in ch_files:
            generate_chapter(f5, cf, speed=args.speed)
    else:
        ch_num = int(args.chapter)
        ch_file = os.path.join(ch_dir, f"chapter_{ch_num:02d}.txt")
        if not os.path.exists(ch_file):
            print(f"Error: Chapter file {ch_file} not found!")
            sys.exit(1)
        generate_chapter(f5, ch_file, speed=args.speed)

if __name__ == "__main__":
    main()
