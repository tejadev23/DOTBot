import streamlit as st
import json
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from datetime import datetime, timedelta
from rapidfuzz import fuzz

# Load data
from assets.standards_metadata import standards_metadata
from assets.contractor_directory import contractor_directory
from assets.gdot_specifications import gdot_specifications as specifications

# Optionally rename
standards = standards_metadata
contractors = contractor_directory

# ------------------------- INTENT & ENTITY PARSER -------------------------
def parse_intent_and_entities(query):
    """
    Analyzes the user's query and extracts intent, value(s), and extra data.
    Supports: vendor number, work class, expiry window, status, field lookups, fuzzy name, location, etc.
    """
    q = query.lower()
    intent = None
    value = None
    extra = {}

    # Vendor number lookup (by name or number)
    if "vendor number" in q:
        intent = "vendor_number_lookup"
        value = re.sub(r'vendor number (for|of)?', '', q).strip()

    # Work class by code
    elif "work class" in q or re.search(r'\b\d{3}[a-zA-Z]*\b', q):
        intent = "work_class"
        match = re.search(r'\b\d{3}[a-zA-Z]*\b', q)
        if match:
            value = match.group(0)
        else:
            value = q

    # Expiry window queries
    elif "expire" in q or "expiring" in q or "expiry" in q:
        if "before" in q:
            intent = "expiry_before"
            match = re.search(r'before\s+(\w+\s+\d{4})', q)
            if match:
                value = match.group(1)
        elif "after" in q:
            intent = "expiry_after"
            match = re.search(r'after\s+(\w+\s+\d{4})', q)
            if match:
                value = match.group(1)
        else:
            intent = "expiry_relative"
            match = re.search(r'(\d+)\s*days', q)
            value = int(match.group(1)) if match else 90

    # Detail view
    elif any(key in q for key in ["details for", "info about", "show me details for"]):
        intent = "vendor_detail"
        value = re.sub(r'details for|info about|show me details for', '', q).strip()

    # Count queries
    elif any(key in q for key in ["how many", "number of"]):
        intent = "count_query"
        value = q

    # Email or phone field queries
    elif "email for" in q:
        intent = "field_lookup"
        value = "email"
        extra["target"] = q.replace("email for", "").strip()
    elif "phone number for" in q:
        intent = "field_lookup"
        value = "phone"
        extra["target"] = q.replace("phone number for", "").strip()

    # Location queries (city/state detection)
    elif any(kw in q for kw in ["in ", "located in", "from"]):
        intent = "location_query"
        match = re.search(r'(in|from|located in)\s+([a-zA-Z\s]+)', q)
        value = match.group(2).strip() if match else q

    # Status queries (e.g., registered only, prequalified vendors)
    elif "registered" in q:
        intent = "status_filter"
        value = "Registered"
    elif "prequalified" in q or "pre-qualified" in q:
        intent = "status_filter"
        value = "Prequalified"

    # Field summary queries
    elif "list all emails" in q or "vendor emails" in q:
        intent = "field_summary"
        value = "email"
    elif "list all phone numbers" in q or "vendor phones" in q:
        intent = "field_summary"
        value = "phone"

    # Work class by fuzzy description (e.g., "fiber optic", "grassing")
    elif any(keyword in q for keyword in ["fiber", "boring", "grassing", "grading", "planting", "pipe", "lighting", "sign"]):
        intent = "work_class_fuzzy_desc"
        value = q.strip()

    # Fallback fuzzy name match
    else:
        intent = "fuzzy_vendor_name"
        value = q.strip()

    return {"intent": intent, "value": value, "extra": extra}

# ------------------------- SEARCH CONTRACTORS -------------------------
def search_contractors(query):
    parsed = parse_intent_and_entities(query)
    intent = parsed["intent"]
    value = parsed["value"]
    results = []
    today = datetime.today()

    value = value.lower()

    for contractor in contractors:
        name = (contractor.get("Vendor Name") or "").lower()
        cname = (contractor.get("Contractor Name") or "").lower()
        vnum = contractor.get("Vendor Number") or ""
        wclasses = contractor.get("Work Classes") or []
        wclass_str = " ".join(wclasses).lower()
        expiry_str = contractor.get("Prequalification Expiry")

        # Fuzzy logic for vendor name
        if intent in ["vendor_detail", "fuzzy_vendor_name"]:
            score = fuzz.partial_ratio(value, name)
            cname_score = fuzz.partial_ratio(value, cname)
            best_score = max(score, cname_score)

            if best_score >= 85:
                contractor["__match_score"] = best_score
                results.append(contractor)

        # Vendor number or name lookup
        elif intent == "vendor_number_lookup":
            if fuzz.partial_ratio(value, name) > 85 or fuzz.partial_ratio(value, cname) > 85 or value == vnum:
                contractor["__highlight"] = f"The Vendor Number for **{contractor['Vendor Name']}** is **{vnum}**."
                results.append(contractor)

        # Exact match work class code
        elif intent == "work_class":
            if value in wclass_str:
                results.append(contractor)

        # Fuzzy match work class by description
        elif intent == "work_class_fuzzy_desc":
            for wc in wclasses:
                parts = wc.split("–", 1)
                if len(parts) == 2:
                    desc = parts[1].strip().lower()
                    if fuzz.partial_ratio(value, desc) > 75:
                        results.append(contractor)
                        break

        # Relative expiry filter
        elif intent == "expiry_relative":
            try:
                expiry_date = datetime.strptime(expiry_str, "%b-%d-%Y")
                if expiry_date <= today + timedelta(days=value):
                    results.append(contractor)
            except:
                continue

        # Expiry before specific month/year
        elif intent == "expiry_before":
            try:
                target_date = datetime.strptime(value, "%B %Y")
                expiry_date = datetime.strptime(expiry_str, "%b-%d-%Y")
                if expiry_date < target_date:
                    results.append(contractor)
            except:
                continue

        # Expiry after specific month/year
        elif intent == "expiry_after":
            try:
                target_date = datetime.strptime(value, "%B %Y")
                expiry_date = datetime.strptime(expiry_str, "%b-%d-%Y")
                if expiry_date > target_date:
                    results.append(contractor)
            except:
                continue

    return results

# ------------------------- DISPLAY RESULTS -------------------------
def show_contractor_results(results):
    for res in results:
        if "__highlight" in res:
            st.success(res["__highlight"])
        st.subheader(f"🏗️ {res['Vendor Name']}")
        st.markdown(f"""
        **Vendor Number**: {res.get('Vendor Number', 'N/A')}  
        **Contractor Name**: {res.get('Contractor Name', 'N/A')}  
        **Status**: {res.get('Status', 'N/A')}  
        **Shipping Address**: {res.get('Shipping Address', 'N/A')}  
        **Mailing Address**: {res.get('Mailing Address', 'N/A')}  
        **Phone Number**: {res.get('Phone Number', 'N/A')}  
        **Email**: {res.get('Email', 'N/A')}  
        **Prequalification Expiry**: {res.get('Prequalification Expiry', 'N/A')}  
        **Work Classes**:
        """)
        for wc in res.get("Work Classes", []):
            st.markdown(f"- {wc}")
        source = res.get("Source", {})
        st.caption(f"📄 Source: {source.get('Doc', 'Unknown')} – Row {source.get('Row', '?')}")

def show_specification_results(results, return_text=False):
    output = []
    
    for spec in results:
        # Section header
        section_header = f"#### 📘 Section {spec['section_id']} – {spec['section_title']}"
        reference = f"**Reference**: 2021 GDOT Standard Specifications, Page {spec['page_number']}"
        
        # Initialize content
        content = spec.get("content", "")
        
        # Format subsections
        subsection_text = ""
        if spec.get("subsections"):
            subsections = spec["subsections"]
            for sub_id, sub_data in subsections.items():
                subsection_text += f"\n\n**{sub_id} {sub_data['title']}**\n{sub_data['content']}"
        
        content += subsection_text
        
        # Create preview (first 800 characters)
        preview = content[:800].strip()
        preview = re.sub(r'\s+', ' ', preview)
        preview_text = f"> {preview}..."
        
        # Combine for text output
        if return_text:
            section_output = f"{section_header}\n{reference}\n{preview_text}\n\n**Full Section**:\n{content}"
            output.append(section_output)
        else:
            # Render to Streamlit
            st.subheader(f"📘 Section {spec['section_id']} – {spec['section_title']}")
            st.markdown(reference)
            st.markdown(preview_text)
            with st.expander("🔍 View Full Section"):
                st.markdown(content)
    
    if return_text:
        return "\n\n".join(output)

# ------------------------- STANDARDS SEARCH -------------------------
def search_standards(query):
    query = query.lower()
    exact_matches = []
    fuzzy_matches = []

    for standard in standards:
        std_id = standard["standard_id"].lower()
        desc = standard["description"].lower()

        if query == std_id:
            exact_matches.append((100, standard))
            continue

        score_id = fuzz.partial_ratio(query, std_id)
        score_desc = fuzz.partial_ratio(query, desc)

        if score_id > 85 or score_desc > 85:
            fuzzy_matches.append((max(score_id, score_desc), standard))

    results = exact_matches + sorted(fuzzy_matches, key=lambda x: x[0], reverse=True)
    return [r[1] for r in results]

# ------------------------- SPECIFICATIONS SEARCH -------------------------
def search_specifications(query):
    results = []
    query_clean = query.lower().strip()

    # Try to extract direct section number like "Section 149" or "Section 104.03"
    section_match = re.search(r'section\s+(\d{1,3}(?:\.\d{1,2})?)', query_clean)
    if section_match:
        target_section = section_match.group(1)
        # Check if section or subsection exists
        section_id = target_section.split('.')[0]
        if section_id in specifications:
            spec = specifications[section_id]
            if '.' in target_section:
                subsection_id = target_section
                if subsection_id in spec["subsections"]:
                    sub_data = spec["subsections"][subsection_id]
                    return [{
                        "section_id": section_id,
                        "section_title": spec["title"],
                        "page_number": sub_data["page"],
                        "content": f"**{subsection_id} {sub_data['title']}**\n{sub_data['content']}",
                        "subsections": None
                    }]
            else:
                # Return main section
                content = spec.get("content", "")
                if spec.get("subsections"):
                    for sub_id, sub_data in spec["subsections"].items():
                        content += f"\n\n**{sub_id} {sub_data['title']}**\n{sub_data['content']}"
                return [{
                    "section_id": section_id,
                    "section_title": spec["title"],
                    "page_number": spec["page"],
                    "content": content,
                    "subsections": spec["subsections"]
                }]

    # Fallback: fuzzy matching across sections and subsections
    for section_id, spec in specifications.items():
        title = spec["title"].lower()
        score_title = fuzz.partial_ratio(query_clean, title)
        
        # Check main section content
        content = spec.get("content", "").lower()
        score_content = fuzz.partial_ratio(query_clean, content)

        # Check subsections
        subsection_content = ""
        for sub_id, sub_data in spec.get("subsections", {}).items():
            sub_title = sub_data["title"].lower()
            sub_content = sub_data["content"].lower()
            score_sub_title = fuzz.partial_ratio(query_clean, sub_title)
            score_sub_content = fuzz.partial_ratio(query_clean, sub_content)
            if max(score_sub_title, score_sub_content) >= 75:
                subsection_content += f"\n\n**{sub_id} {sub_data['title']}**\n{sub_data['content']}"
                score_content = max(score_content, score_sub_title, score_sub_content)

        # Combine scores
        best_score = max(score_title, score_content)
        if best_score >= 75:
            result = {
                "section_id": section_id,
                "section_title": spec["title"],
                "page_number": spec["page"],
                "content": subsection_content or spec.get("content", ""),
                "subsections": spec["subsections"] if subsection_content else None
            }
            results.append((best_score, result))

    # Sort and limit to top 3 results
    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results[:3]]

# ------------------------- CLEAN DESCRIPTION -------------------------
def clean_description(text):
    text = text.replace("\n", " ").strip()
    text = re.sub(r'[^a-zA-Z0-9.,:/()\-\s]{2,}', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ------------------------- UI -------------------------
from streamlit_chat import message

st.set_page_config(page_title="DOTBot Demo", page_icon="🚧", layout="centered")
st.markdown('<style>' + open('styles.css').read() + '</style>', unsafe_allow_html=True)

st.markdown("<div class='chat-title'>🤖 DOTBot 1.2 (Demo) – GDOT Assistant</div>", unsafe_allow_html=True)

if "selected_module" not in st.session_state:
    st.session_state.selected_module = "GDOT Specifications"

st.session_state.selected_module = st.selectbox(
    "📦 Select a module to search:",
    ["Contractor Directory", "Construction Standards", "GDOT Specifications"],
    index=["Contractor Directory", "Construction Standards", "GDOT Specifications"].index(st.session_state.selected_module)
)

placeholder_text = {
    "Contractor Directory": "Search for contractors, work classes, or expiry details...",
    "Construction Standards": "Search for construction standard IDs or descriptions...",
    "GDOT Specifications": "Search for specification sections (e.g., Section 149)..."
}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! I'm DOTBOT, your GDOT Assistant. Please choose a module and ask your question."}
    ]

for i, msg in enumerate(st.session_state.messages):
    message(msg["content"], is_user=(msg["role"] == "user"), key=str(i))

query = st.chat_input(placeholder_text[st.session_state.selected_module])

if query:
    module = st.session_state.selected_module
    st.session_state.messages.append({"role": "user", "content": query})

    if module == "Contractor Directory":
        results = search_contractors(query)
        if results:
            response = "\n\n".join(
                [f"🏗️ **{r.get('Vendor Name', 'Unknown')}** – "
                 f"Work Class: {', '.join(r.get('Work Classes', []))}, "
                 f"Expiry: {r.get('Prequalification Expiry', 'N/A')}" for r in results]
            )
        else:
            response = "⚠️ No matching contractors found."

    elif module == "Construction Standards":
        results = search_standards(query)
        if results:
            sections = []
            for r in results:
                desc = clean_description(r["description"])
                image_url = f"https://raw.githubusercontent.com/tejadev23/DOTBot/main/data/standards/{r['files'][0]['filename']}"
                sections.append(
                    f"📄 **{r['standard_id']}** – {desc}\n[🔗 View Image]({image_url})"
                )
            response = "### 📐 Construction Standards\n\n" + "\n\n".join(sections)
        else:
            response = "⚠️ No matching standards found."

    elif module == "GDOT Specifications":
        results = search_specifications(query)
        if results:
            response = show_specification_results(results, return_text=True)
        else:
            response = "⚠️ No matching specifications found."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()