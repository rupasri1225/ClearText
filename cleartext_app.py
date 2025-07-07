import streamlit as st
from textblob import TextBlob
import re

# --- Page Configuration ---
st.set_page_config(page_title="ClearText", layout="centered")

# --- Custom CSS for Mobile-Friendly and Stylish Design ---
st.markdown("""
    <style>
        html, body {
            background-color: #f0f2f6;
            font-family: 'Segoe UI', sans-serif;
        }

        .main {
            background-color: #ffffff;
            margin-top: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 12px rgba(0, 0, 0, 0.05);
            max-width: 100%;
        }

        .stTextArea textarea {
            background-color: #fffdf7;
            font-size: 16px;
            color: #333333;
            border-radius: 10px;
            padding: 1rem;
            line-height: 1.6;
        }

        .stButton button {
            background-color: #6a0dad;
            color: white;
            font-weight: 600;
            font-size: 16px;
            border-radius: 10px;
            padding: 0.75rem 1.5rem;
            width: 100%;
            transition: 0.3s ease-in-out;
        }

        .stButton button:hover {
            background-color: #7f3dc9;
        }

        @media (max-width: 768px) {
            .main {
                padding: 1rem;
                margin-top: 1rem;
            }
            .stTextArea textarea {
                font-size: 15px;
            }
        }

        .footer {
            text-align: center;
            font-size: 14px;
            color: gray;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Layout Wrapper ---
st.markdown('<div class="main">', unsafe_allow_html=True)

# --- Title and Description ---
st.markdown("<h1 style='text-align: center;'>ClearText</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #6a0dad;'>AI-Powered Text Cleaner & Formatter</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Make your messy text clean, neat, and professional with just one click!</p>", unsafe_allow_html=True)

# --- Input Text Box ---
text = st.text_area("Paste your messy text here:", height=200)

# --- Option Checkbox ---
remove_specials = st.checkbox("Remove special characters (like !@#$%)", value=True)

# --- Cleaning Logic ---
def clean_text(text):
    cleaned = re.sub(r"\s+", " ", text.strip())
    if remove_specials:
        cleaned = re.sub(r"[^a-zA-Z0-9\s.,!?]", "", cleaned)
    blob = TextBlob(cleaned)
    corrected = blob.correct().string.capitalize()
    return corrected

# --- Clean Button Action ---
if st.button("Clean Text Now"):
    if text:
        result = clean_text(text)
        st.markdown("### Cleaned Output")
        st.success(result)
    else:
        st.warning("Please enter some text.")

# --- Footer Branding ---
st.markdown("</div>", unsafe_allow_html=True)
st.markdown('<div class="footer">Designed with by <b>Yarramsetti Rupa Sri</b></div>', unsafe_allow_html=True)
