import streamlit as st
from textblob import TextBlob
import re

# --- Page Configuration ---
st.set_page_config(page_title="ClearText", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .main {
            background-color: #f7f7f7;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: auto;
        }
        .stTextArea textarea {
            background-color: #fffaf0;
            font-size: 16px;
            color: #333;
            border-radius: 10px;
        }
        .stButton button {
            background-color: #6a0dad;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            height: 50px;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #7d3ac1;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>🧹 ClearText</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #6a0dad;'>AI-Powered Text Cleaner & Formatter</h4>", unsafe_allow_html=True)
st.markdown("Enhance your writing by cleaning and formatting unstructured or messy text.", unsafe_allow_html=True)
st.markdown("")

# --- Text Input ---
text = st.text_area("Paste your messy text here:", height=200)

# --- Option ---
remove_specials = st.checkbox("Remove special characters (!@#$%)", value=True)

# --- Function to Clean Text ---
def clean_text(text):
    cleaned = re.sub(r"\s+", " ", text.strip())
    if remove_specials:
        cleaned = re.sub(r"[^a-zA-Z0-9\s.,!?]", "", cleaned)
    blob = TextBlob(cleaned)
    corrected = blob.correct().string.capitalize()
    return corrected

# --- Button Action ---
if st.button("Clean Text Now"):
    if text:
        result = clean_text(text)
        st.markdown("###  Cleaned Output")
        st.success(result)
    else:
        st.warning("Please enter some text.")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Designed by <b>Yarramsetti Rupa Sri</b></p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
