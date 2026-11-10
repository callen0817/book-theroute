import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def extract_docx_text(docx_path):
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    text = []
    with zipfile.ZipFile(docx_path) as docx:
        with docx.open('word/document.xml') as f:
            tree = ET.parse(f)
            root = tree.getroot()
            for para in root.iter(f"{{{namespaces['w']}}}p"):
                para_text = []
                for run in para.iter(f"{{{namespaces['w']}}}r"):
                    for t in run.iter(f"{{{namespaces['w']}}}t"):
                        if t.text:
                            para_text.append(t.text)
                if para_text:
                    text.append(''.join(para_text))
    return '\n'.join(text)

if __name__ == "__main__":
    for f in ["The Route.docx", "The Route_Summary.docx"]:
        path = os.path.join("c:/Users/callen/OneDrive - Reisource/Desktop/The Route", f)
        if os.path.exists(path):
            try:
                txt = extract_docx_text(path)
                out_name = path.replace('.docx', '.txt')
                with open(out_name, 'w', encoding='utf-8') as out_f:
                    out_f.write(txt)
                print(f"Extracted {f} to {out_name}")
            except Exception as e:
                print(f"Error extracting {f}: {e}")
        else:
            print(f"File not found: {path}")
