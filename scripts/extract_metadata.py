import os
import cv2
import pytesseract
import json
import re

# ✅ SET this to your Tesseract install path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ✅ Path to your construction standard image folder
image_folder = r"C:\Users\home\Desktop\New folder\CSD- Images"

# ✅ Placeholder base URL (update later when you host images)
base_url = "https://yourdomain.com/downloads/standards/"

# ✅ Output file path
output_file = "standards_metadata.json"

def crop_detail_box(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error reading image: {image_path}")
        return None
    h, w = img.shape[:2]
    
    # Refined bottom-right box crop
    x1, y1 = int(w * 0.759), int(h * 0.803)
    x2, y2 = int(w * 0.98), int(h * 0.98)

    cropped = img[y1:y2, x1:x2]
    return cropped

def extract_text(cropped_img):
    return pytesseract.image_to_string(cropped_img)

def parse_standard_info(text):
    lines = text.splitlines()
    capture = False
    description_lines = []

    # Start capture if one of these is found
    start_keywords = ["CONSTRUCTION DETAIL", "CONSTRUCTION DETAILS", "STANDARD"]
    # Stop capture if one of these is found
    stop_keywords = ["REVISION", "NO SCALE", "NUMBER", "BY", "NOVEMBER", "DATE", "DRAWN", "CHECKED", "TRACED"]

    for line in lines:
        upper_line = line.strip().upper()

        if not capture:
            if any(start_key in upper_line for start_key in start_keywords):
                capture = True
                continue
        else:
            if any(stop_key in upper_line for stop_key in stop_keywords):
                break
            if upper_line.strip() == "":
                continue
            description_lines.append(line.strip())

    description = "\n".join(description_lines).strip()
    return description if description else "No description found"


def build_metadata(image_folder):
    metadata = []
    seen_ids = {}  # To handle duplicates

    for filename in os.listdir(image_folder):
        if filename.lower().endswith(".jpg"):
            filepath = os.path.join(image_folder, filename)
            cropped = crop_detail_box(filepath)
            if cropped is None:
                continue
            text = extract_text(cropped)
            print(f"\n🧾 OCR result for {filename}:\n{text}")
            standard_id = os.path.splitext(filename)[0].upper()  # From filename like TS-08.jpg
            desc = parse_standard_info(text)
            if standard_id:
                if standard_id not in seen_ids:
                    entry = {
                        "standard_id": standard_id,
                        "description": desc,
                        "files": []
                    }
                    metadata.append(entry)
                    seen_ids[standard_id] = entry
                seen_ids[standard_id]["files"].append({
                    "filename": filename,
                    "url": f"{base_url}{filename}"
                })
            else:
                print(f"❌ Could not extract standard ID from: {filename}")
    return metadata

# Run it
metadata = build_metadata(image_folder)

# Save the result
with open(output_file, "w") as f:
    json.dump(metadata, f, indent=4)

print(f"✅ Metadata saved to {output_file} with {len(metadata)} unique standards.")
