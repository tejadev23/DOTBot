import streamlit as st
import json
import re
from datetime import datetime, timedelta
from rapidfuzz import fuzz

# Load data
with open("standards_metadata.json", "r") as f:
    standards = json.load(f)
with open("contractor_directory.json", "r") as f:
    contractors = json.load(f)

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
            # Get highest fuzzy match across all contractors
            score = fuzz.partial_ratio(value, name)
            cname_score = fuzz.partial_ratio(value, cname)
            best_score = max(score, cname_score)

            # Keep only strong matches (>85), perfect matches first
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

        # Fuzzy match work class by description (NEW!)
        elif intent == "work_class_fuzzy_desc":
            for wc in wclasses:
                parts = wc.split("–", 1)
                if len(parts) == 2:
                    desc = parts[1].strip().lower()
                    if fuzz.partial_ratio(value, desc) > 75:
                        results.append(contractor)
                        break

        # Relative expiry filter
        # Relative expiry (e.g., expiring in 90 days)
        elif intent == "expiry_relative":
            try:
                expiry_date = datetime.strptime(expiry_str, "%b-%d-%Y")
                if expiry_date <= today + timedelta(days=value):
                    results.append(contractor)
            except:
                continue

        # Expiry before specific month/year (e.g., before Sept 2025)
        elif intent == "expiry_before":
            try:
                target_date = datetime.strptime(value, "%B %Y")
                expiry_date = datetime.strptime(expiry_str, "%b-%d-%Y")
                if expiry_date < target_date:
                    results.append(contractor)
            except:
                continue

        # Expiry after specific month/year (e.g., after July 2024)
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

# ------------------------- CLEAN DESCRIPTION -------------------------
def clean_description(text):
    text = text.replace("\n", " ").strip()
    text = re.sub(r'[^a-zA-Z0-9.,:/()\-\s]{2,}', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ------------------------- UI -------------------------
st.set_page_config(page_title="DOTBot Demo", page_icon="🚧")
st.title("🤖 DOTBot 1.2(Demo) – GDOT Assistant")

query = st.text_input("Ask anything from Vendor Directory or about Construction Standards:")

if query:
    if any(word in query.lower() for word in ["vendor", "contractor", "class", "expire", "detail", "number", "info"]):
        contractor_results = search_contractors(query)
        if contractor_results:
            show_contractor_results(contractor_results)
        else:
            st.warning("No matching contractors found.")
    else:
        standard_results = search_standards(query)
        if standard_results:
            for res in standard_results:
                st.subheader(f"📄 {res['standard_id']}")
                desc_clean = clean_description(res["description"])
                st.markdown(f"**{res['standard_id']}** is the Construction Standard for **{desc_clean}**.")

                filename = res["files"][0]["filename"]
                raw_img_url = f"https://raw.githubusercontent.com/tejadev23/DOTBot/main/data/standards/{filename}"
                st.markdown(f"[🔗 View Image in GitHub]({raw_img_url})")
                st.image(raw_img_url, width=500)
        else:
            st.warning("No results found. Try a different keyword.")