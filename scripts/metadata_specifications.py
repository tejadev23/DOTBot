import fitz  # PyMuPDF
import re
import json

# Path to the PDF file
PDF_PATH = r"C:\Users\home\OneDrive\Desktop\DOTBot data\Basic-Standard Specifications\Section 160 Erosion Control\2021StandardSpecifications.pdf"

# Pattern to match section headers like "Section 149 — Construction Layout"
SECTION_PATTERN = re.compile(r"(Section\s+(\d{3})\s+[-–—]\s+(.*))", re.IGNORECASE)

# Open the PDF
doc = fitz.open(PDF_PATH)

# Step 1: Extract text page-by-page with page numbers
pages = []
for i in range(len(doc)):
    text = doc[i].get_text()
    pages.append({
        "page_number": i + 1,
        "text": text
    })

# Step 2: Identify sections by scanning for section headers
sections = []

# Skip the Table of Contents and early pages (usually first 10 pages)
MIN_BODY_PAGE = 10

for idx, page in enumerate(pages):
    if page["page_number"] < MIN_BODY_PAGE:
        continue  # skip TOC and front matter

    matches = SECTION_PATTERN.findall(page["text"])
    for match in matches:
        full_title, section_id, section_title = match
        sections.append({
            "section_id": int(section_id),
            "section_title": section_title.strip(),
            "start_page": page["page_number"],
            "full_title": full_title.strip()
        })

# Step 3: Add end_page to each section
for i in range(len(sections)):
    if i < len(sections) - 1:
        sections[i]["end_page"] = sections[i + 1]["start_page"] - 1
    else:
        sections[i]["end_page"] = len(doc)

# Step 4: Extract section text content
for section in sections:
    start = section["start_page"] - 1
    end = section["end_page"]
    content = "\n".join([pages[i]["text"] for i in range(start, end)])
    section["content"] = content.strip()

# Step 5: Export as JSON or Python list
metadata_chunks = []
for s in sections:
    metadata_chunks.append({
        "section_id": s["section_id"],
        "section_title": s["section_title"],
        "page_number": s["start_page"],
        "content": s["content"]
    })

# Optional: Save as .py or .json
with open("spec_sections.py", "w", encoding="utf-8") as f:
    f.write("sections = ")
    json.dump(metadata_chunks, f, indent=2)

print(f"✅ Extracted {len(metadata_chunks)} sections. Output saved to 'spec_sections.py'")
