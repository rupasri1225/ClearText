import streamlit as st
from textblob import TextBlob
import re

# --- App Config ---
st.set_page_config(page_title="ClearText", layout="centered")
st.title("🧹 ClearText: AI-Powered Text Cleaner")
st.markdown("Enhance your writing by removing extra spaces, fixing grammar, and formatting text like a pro!")

# --- User Input ---
text = st.text_area("📋 Paste your messy text here:", height=200)

# --- Options ---
remove_specials = st.checkbox("Remove special characters (!@#$%)", value=True)

# --- Cleaning Function ---
def clean_text(text):
    # Step 1: Remove extra spaces
    cleaned = re.sub(r"\s+", " ", text.strip())
    
    # Step 2: Remove special characters if chosen
    if remove_specials:
        cleaned = re.sub(r"[^a-zA-Z0-9\s.,!?]", "", cleaned)
    
    # Step 3: Grammar & Spelling correction
    blob = TextBlob(cleaned)
    corrected = blob.correct().string.capitalize()
    
    return corrected

# --- Button ---
if st.button("🧼 Clean Text Now"):
    if text:
        result = clean_text(text)
        st.markdown("### ✅ Cleaned Output")
        st.success(result)
    else:
        st.warning("Please enter some text.")
