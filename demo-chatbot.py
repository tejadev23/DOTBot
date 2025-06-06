import streamlit as st
import json
import re
from rapidfuzz import fuzz

# Load metadata
with open("standards_metadata.json", "r") as f:
    standards = json.load(f)

# Fuzzy search function
def search_standards(query):
    query = query.lower()
    exact_matches = []
    fuzzy_matches = []

    for standard in standards:
        std_id = standard["standard_id"].lower()
        desc = standard["description"].lower()

        # Priority 1: exact match
        if query == std_id:
            exact_matches.append((100, standard))
            continue

        # Priority 2: partial fuzzy match
        score_id = fuzz.partial_ratio(query, std_id)
        score_desc = fuzz.partial_ratio(query, desc)

        if score_id > 85 or score_desc > 85:
            fuzzy_matches.append((max(score_id, score_desc), standard))

    # Combine exact matches (on top) + sorted fuzzy matches
    results = exact_matches + sorted(fuzzy_matches, key=lambda x: x[0], reverse=True)
    return [r[1] for r in results]


# Description cleanup function
def clean_description(text):
    text = text.replace("\n", " ").strip()
    text = re.sub(r'[^a-zA-Z0-9.,:/()\-\s]{2,}', '', text)  # remove weird symbols
    text = re.sub(r'\s+', ' ', text)                        # remove extra spaces
    text = re.sub(r'\b(?:hi|fam|way)\b', '', text, flags=re.IGNORECASE)
    return text.strip()

# Streamlit UI
st.set_page_config(page_title="DOTBot Demo", page_icon="🚧")
st.title("🤖 DOTBot – GDOT Standard Search Demo")

query = st.text_input("Ask me about a standard drawing (e.g., TS-10A, manhole, fiber optics):")

if query:
    results = search_standards(query)
    if results:
        for res in results:
            st.subheader(f"📄 {res['standard_id']}")

            # Clean and show description
# Construct better response
            standard_id = res["standard_id"]
            desc_clean = clean_description(res["description"])
            highlighted_response = f"**{standard_id}** is the Construction Standard for **{desc_clean}**."

# Show formatted result
            st.markdown(highlighted_response)

# Show image and link
            filename = res["files"][0]["filename"]
            raw_img_url = f"https://raw.githubusercontent.com/tejadev23/DOTBot/main/data/standards/{filename}"
            st.markdown(f"[🔗 View Image in GitHub]({raw_img_url})")
            st.image(raw_img_url, width=500)

    else:
        st.warning("No results found. Try a different keyword.")
