import streamlit as st
import json
import os

# Load metadata
with open("standards_metadata.json", "r") as f:
    standards = json.load(f)

# Build a simple search function
def search_standards(query):
    results = []
    for standard in standards:
        std_id = standard["standard_id"].lower()
        desc = standard["description"].lower()
        if query.lower() in std_id or query.lower() in desc:
            results.append(standard)
    return results

# Streamlit UI
st.set_page_config(page_title="DOTBot Demo", page_icon="🚧")
st.title("🤖 DOTBot – GDOT Standard Search Demo")

query = st.text_input("Ask me about a standard drawing (e.g., TS-10A, manhole, fiber optics):")

if query:
    results = search_standards(query)
    if results:
        for res in results:
            st.subheader(f"📄 {res['standard_id']}")
            st.markdown(res["description"].replace("\n", " "))
            img_path = os.path.join("CSD- Images", "test", res["files"][0]["filename"])  # adjust folder name
            if os.path.exists(img_path):
                st.image(img_path, width=500)
    else:
        st.warning("No results found. Try a different keyword.")