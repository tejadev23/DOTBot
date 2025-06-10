from docx import Document
import json

# Load the Word document
doc_path = "Contractor Directory Split Word Doc.docx"  # Update if filename differs
doc = Document(doc_path)

# Prepare variables
contractors = []
current_contractor = {}
work_classes = []
row_counter = 1  # Acts like row reference in source

# Loop through each paragraph
for para in doc.paragraphs:
    text = para.text.strip()
    if not text:
        continue

    # Start of a new contractor
    if text.startswith("Vendor: "):
        if current_contractor:
            current_contractor["Work Classes"] = work_classes
            current_contractor["Source"] = {
                "Doc": "Contractor Directory Split Word Doc.docx",
                "Row": row_counter
            }
            contractors.append(current_contractor)
            row_counter += 1

        current_contractor = {
            "Vendor Name": text.replace("Vendor: ", ""),
            "Vendor Number": None,
            "Contractor Name": None,
            "Status": None,
            "Shipping Address": None,
            "Mailing Address": None,
            "Phone Number": None,
            "Email": None,
            "Prequalification Expiry": None
        }
        work_classes = []

    elif text.startswith("Vendor Number:"):
        current_contractor["Vendor Number"] = text.replace("Vendor Number:", "").strip()
    elif text.startswith("Contractor Name:"):
        current_contractor["Contractor Name"] = text.replace("Contractor Name:", "").strip()
    elif text.startswith("Status:"):
        current_contractor["Status"] = text.replace("Status:", "").strip()
    elif text.startswith("Shipping Address:"):
        current_contractor["Shipping Address"] = text.replace("Shipping Address:", "").strip()
    elif text.startswith("Mailing Address:"):
        current_contractor["Mailing Address"] = text.replace("Mailing Address:", "").strip()
    elif text.startswith("Phone Number:"):
        current_contractor["Phone Number"] = text.replace("Phone Number:", "").strip()
    elif text.startswith("Email:"):
        current_contractor["Email"] = text.replace("Email:", "").strip()
    elif text.startswith("Prequalification Expiry:"):
        current_contractor["Prequalification Expiry"] = text.replace("Prequalification Expiry:", "").strip()
    elif text.startswith("•") or text.startswith("-") or "–" in text:
        work_classes.append(text.strip("•- ").strip())

# Don't forget to add the last contractor
if current_contractor:
    current_contractor["Work Classes"] = work_classes
    current_contractor["Source"] = {
        "Doc": "Contractor Directory Split Word Doc.docx",
        "Row": row_counter
    }
    contractors.append(current_contractor)

# Save to JSON
output_file = "contractor_directory.json"
with open(output_file, "w") as f:
    json.dump(contractors, f, indent=2)

print(f"✅ Converted {len(contractors)} contractors to {output_file}")
