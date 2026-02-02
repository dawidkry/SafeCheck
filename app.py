import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# 2. Force Dark Mode CSS
st.markdown("""
    <style>
    /* Hide Streamlit UI Decorations */
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display:none;}
    
    /* Force Background Color */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }

    /* Style the Text Area for Dark Mode */
    .stTextArea textarea { 
        border-radius: 15px; 
        border: 2px solid #30363D; 
        padding: 10px;
        font-size: 16px;
        background-color: #161B22 !important;
        color: white !important;
    }

    /* Adjust titles and captions for Dark Mode */
    h1, h2, h3, p, span, .stMarkdown {
        color: white !important;
    }
    
    /* Make the divider subtle */
    hr {
        border-top: 1px solid #30363D !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Time Handling
now = datetime.now()
timestamp = now.strftime("%I:%M %p")

# 4. App Content
st.title("🛡️ SafeCheck")

DEFAULT_MSG = f"I am okay, safe, and all is good in life! ❤️\n(Sent at {timestamp})"
custom_message = st.text_area("Final Message Preview:", value=DEFAULT_MSG, height=140)
encoded_msg = urllib.parse.quote(custom_message)

st.write("### Choose your app:")

# 5. The Grid
html_lines = [
    '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-family: sans-serif;">',
    
    # WhatsApp
    f'<a href="whatsapp://send?text={encoded_msg}" style="text-decoration:none;">',
    '<div style="background-color:#25D366; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">',
    '<img src="https://img.icons8.com/material-outlined/48/ffffff/whatsapp.png" width="28" height="28"/>WhatsApp</div></a>',
    
    # iMessage
    f'<a href="sms:&body={encoded_msg}" style="text-decoration:none;">',
    '<div style="background-color:#007AFF; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">',
    '<img src="https://img.icons8.com/ios-filled/50/ffffff/speech-bubble.png" width="24" height="24"/>iMessage</div></a>',
