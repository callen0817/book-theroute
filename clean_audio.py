import os
import subprocess
import soundfile as sf
import numpy as np
import noisereduce as nr

def clean_recording():
    raw_path = "Cairo_Voice_Sample.wav"
    cleaned_path = "Cairo_Voice_Cleaned.wav"
    cleaned_mp3 = "Cairo_Voice_Cleaned.mp3"
    
    print(f"Loading {raw_path}...")
    data, sr = sf.read(raw_path)
    print(f"Loaded: {len(data)/sr:.2f} seconds, {sr} Hz")
    
    # 1. Noise reduction using room ambient silence (first 2.2 seconds)
    print("Step 1: Analyzing ambient room tone and applying spectral gating...")
    noise_sample = data[:int(sr * 2.2)]
    denoised = nr.reduce_noise(
        y=data,
        sr=sr,
        y_noise=noise_sample,
        prop_decrease=0.80,
        n_fft=2048,
        stationary=True
    )
    
    temp_wav = "temp_denoised.wav"
    sf.write(temp_wav, denoised, sr)
    
    # 2. FFmpeg Mastering Chain:
    # - highpass=f=90: cut low frequency room rumbles and plosive air
    # - equalizer=f=380: cut boxy hollow room bounce (-4dB)
    # - equalizer=f=7000: tame harsh piercing highs (-3.5dB)
    # - deesser=i=0.85: dynamic sibilance tamer (attenuates sharp S/SH/CH bursts)
    # - agate=threshold=-32dB: downward expander to cut reverberation tails and room echo
    # - volume normalization
    ffmpeg_bin = r"C:\Users\ChristopherAllen\audiobook_env\Lib\site-packages\static_ffmpeg\bin\win32\ffmpeg.EXE"
    filter_chain = (
        "highpass=f=90,"
        "equalizer=f=380:width_type=o:w=1.5:g=-4.0,"
        "equalizer=f=7000:width_type=o:w=1.2:g=-3.5,"
        "deesser=i=0.88:m=0.5:f=0.5:s=o,"
        "agate=threshold=-32dB:ratio=2.5:attack=10:release=110,"
        "volume=1.8"
    )
    
    print("Step 2: Applying de-esser, anti-echo acoustic gate, and parametric EQ...")
    cmd = [
        ffmpeg_bin, "-y",
        "-i", temp_wav,
        "-af", filter_chain,
        cleaned_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error during processing:", res.stderr)
        return
        
    # Also export MP3 for easy listening
    subprocess.run([ffmpeg_bin, "-y", "-i", cleaned_path, "-codec:a", "libmp3lame", "-b:a", "192k", cleaned_mp3], capture_output=True)
    
    # Clean up temp
    if os.path.exists(temp_wav):
        os.remove(temp_wav)
        
    print(f"\n[SUCCESS] Cleaned master saved as: {cleaned_path} and {cleaned_mp3}")
    
    # Also extract the clean 5.5-second reference slice from the cleaned audio
    cleaned_data, c_sr = sf.read(cleaned_path)
    start = int(2.70 * c_sr)
    clean_ref = cleaned_data[start : int(8.20 * c_sr)]
    ref_out = "ref_voice_first_sentence.wav"
    sf.write(ref_out, clean_ref, c_sr)
    print(f"[SUCCESS] Updated reference slice for voice cloner: {ref_out}")

if __name__ == "__main__":
    clean_recording()
