import os
import re

input_file = "The Route.txt"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# The pattern looks for "Chapter X" or "Chapter X —" or "Chapter X –"
# But we can also just split by "Chapter " if it's the start of a line.

chapters = re.split(r'\n(?=Chapter \d+)', text)

os.makedirs("chapters", exist_ok=True)

print(f"Total parts found: {len(chapters)}")

for i, chapter_text in enumerate(chapters):
    if i == 0 and "Chapter" not in chapter_text:
        # This is the front matter (Title, TOC, etc.)
        filename = "chapters/00_front_matter.txt"
    else:
        # Extract chapter number
        match = re.search(r'Chapter (\d+)', chapter_text)
        if match:
            num = int(match.group(1))
            filename = f"chapters/chapter_{num:02d}.txt"
        else:
            filename = f"chapters/part_{i:02d}.txt"
            
    with open(filename, "w", encoding="utf-8") as f:
        f.write(chapter_text.strip() + "\n")
        
print("Splitting complete.")
