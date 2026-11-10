import os
import re
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Folder paths
CHAPTERS_DIR = r"c:\Users\callen\OneDrive - Reisource\Desktop\The Route\chapters"
OUTPUT_FILE = r"c:\Users\callen\OneDrive - Reisource\Desktop\The Route\The_Route_Final.docx"

# Chapter opening variations
OPENINGS = ["The trail", "Our route", "The journey", "The ground", "The terrain", "The way"]
opening_idx = 0

def apply_systematic_changes(text, chapter_num):
    global opening_idx
    
    # 1. Vary chapter openings if they start with "The path "
    # We look for "The path " at the start of a paragraph (after chapter title)
    if "The path " in text and opening_idx < len(OPENINGS):
        # Only replace the first instance to vary openings
        text = text.replace("The path ", OPENINGS[opening_idx] + " ", 1)
        opening_idx = (opening_idx + 1) % len(OPENINGS)

    # 2. Capitalize Keeper
    text = re.sub(r'\bkeeper\b', 'Keeper', text)
    text = re.sub(r'\bkeepers\b', 'Keepers', text)
    
    # Capitalize Archivist
    text = re.sub(r'\barchivist\b', 'Archivist', text)
    text = re.sub(r'\barchivists\b', 'Archivists', text)

    # 3. Capitalize "the knotted" before realization, then lowercase/quotes
    if chapter_num < 23:
        text = re.sub(r'\bthe knotted\b', 'The Knotted', text, flags=re.IGNORECASE)
    else:
        text = re.sub(r'\bthe knotted\b', '"the knotted"', text, flags=re.IGNORECASE)

    # 4. Space out moral lessons by replacing explicit "lesson" callouts
    text = text.replace("The lesson is sharp:", "The truth is sharp:")
    text = text.replace("The lesson is immediate, brutal", "The realization is immediate, brutal")
    text = text.replace("The lesson is immediate and visceral:", "The realization is immediate and visceral:")
    text = text.replace("I realize the lesson:", "I realize:")
    text = text.replace("The lesson remains:", "The truth remains:")
    text = text.replace("Slowly, I understand the lesson.", "Slowly, I understand.")
    text = text.replace("I sense a lesson deeper", "I sense a truth deeper")
    text = text.replace("echoes lessons we carry", "echoes memories we carry")
    text = text.replace("absorbing lessons", "absorbing knowledge")

    # 5. Italicize inner thoughts (known occurrences)
    thoughts = [
        "Walk your own path. You are ready.",
        "Walk your path. Keep your eyes and mind open.",
        "Not human hands, I think.",
        "Not a bird either."
    ]
    for t in thoughts:
        text = text.replace(t, f"*{t}*")

    return text

def main():
    doc = Document()

    # Set page size (4.25 x 6.87) and margins (1 inch)
    for section in doc.sections:
        section.page_width = Inches(4.25)
        section.page_height = Inches(6.87)
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # 1. Blank first page for cover art
    doc.add_page_break()

    # 2. Title page
    doc.add_paragraph() # Spacing
    doc.add_paragraph()
    title = doc.add_paragraph("The Route")
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.runs[0].font.size = Pt(24)
    title.runs[0].bold = True
    
    doc.add_paragraph()
    author = doc.add_paragraph("Black P. Pull")
    author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    author.runs[0].font.size = Pt(14)
    
    doc.add_page_break()

    # 3. Table of Contents
    toc_title = doc.add_heading("Table of Contents", level=1)
    toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    chapters = sorted(os.listdir(CHAPTERS_DIR), key=lambda x: int(re.search(r'\d+', x).group()))
    
    for ch_file in chapters:
        with open(os.path.join(CHAPTERS_DIR, ch_file), 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            # TOC entry
            doc.add_paragraph(first_line)

    doc.add_page_break()

    # 4. Empty Foreword
    foreword = doc.add_heading("Foreword", level=1)
    foreword.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_page_break()

    # 5. Empty Acknowledgements
    ack = doc.add_heading("Acknowledgements", level=1)
    ack.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_page_break()

    # 6. Chapters and Parts
    current_part = None
    
    for ch_file in chapters:
        chapter_num = int(re.search(r'\d+', ch_file).group())
        
        with open(os.path.join(CHAPTERS_DIR, ch_file), 'r', encoding='utf-8') as f:
            content = f.read()

        lines = content.strip().split('\n')
        if not lines:
            continue
            
        chapter_header = lines[0].strip()
        body_text = '\n'.join(lines[1:]).strip()
        
        # Determine part from the header (e.g., "Chapter 1 - Embers: ...")
        part_match = re.search(r'–\s*([^:]+):', chapter_header)
        if not part_match:
            part_match = re.search(r'—\s*([^:]+)', chapter_header) # some use em-dash without colon

        part_name = part_match.group(1).strip() if part_match else "Novel"
        
        # If new part, add Part Header on its own page
        if part_name != current_part and ":" in chapter_header:
            current_part = part_name
            # Part header page
            doc.add_paragraph()
            doc.add_paragraph()
            part_heading = doc.add_heading(f"Part: {current_part}", level=1)
            part_heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_page_break()
            
        # Apply edits
        body_text = apply_systematic_changes(body_text, chapter_num)
        
        # Add Chapter Header
        ch_heading = doc.add_heading(chapter_header, level=2)
        ch_heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Add Chapter body paragraphs
        for paragraph in body_text.split('\n'):
            if paragraph.strip():
                # Handling italics for inner thoughts
                p = doc.add_paragraph()
                # Simple markdown-like italics parsing for *text*
                parts = re.split(r'(\*[^*]+\*)', paragraph.strip())
                for part in parts:
                    if part.startswith('*') and part.endswith('*'):
                        run = p.add_run(part[1:-1])
                        run.italic = True
                    else:
                        p.add_run(part)
        
        doc.add_page_break()

    doc.save(OUTPUT_FILE)
    print(f"Successfully generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
