import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# 2. Permanent Dark Mode CSS
st.markdown("""
    <style>
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display:none;}
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stTextArea textarea { 
        border-radius: 15px; border: 2px solid #30363D; 
        background-color: #161B22 !important; color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Time Handling
now = datetime.now()
timestamp = now.strftime("%I:%M %p")

# 4. Content Logic
st.title("🛡️ SafeCheck")
DEFAULT_MSG = f"I am okay, safe, and all is good in life! ❤️\n(Sent at {timestamp})"
custom_message = st.text_area("Message Preview:", value=DEFAULT_MSG, height=140)
encoded_msg = urllib.parse.quote(custom_message)

st.write("### Choose your app:")

# 5. The Grid (Using Double Quotes for Python strings)
h = []
h.append("<div style='display:grid; grid-template-columns:1fr 1fr; gap:12px; font-family:sans-serif;'>")

# WhatsApp
h.append("<a href='whatsapp://send?text=" + encoded_msg + "' target='_top' style='text-decoration:none;'>")
h.append("<div style='background-color:#25D366; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; box-shadow:0 4px 10px rgba(0,0,0,0.3);'>")
h.append("<img src='https://img.icons8.com/material-outlined/48/ffffff/whatsapp.png' width='28' height='28'/>WhatsApp</div></a>")

# iMessage
h.append("<a href='sms:&body=" + encoded_msg + "' target='_top' style='text-decoration:none;'>")
h.append("<div style='background-color:#007AFF; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; box-shadow:0 4px 10px rgba(0,0,0,0.3);'>")
h.append("<img src='https://img.icons8.com/ios-filled/50/ffffff/speech-bubble.png' width='24' height='24'/>iMessage</div></a>")

# Viber
h.append("<a href='viber://forward?text=" + encoded_msg + "' target='_top' style='text-decoration:none;'>")
h.append("<div style='background-color:#7360F2; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; box-shadow:0 4px 10px rgba(0,0,0,0.3);'>")
h.append("<img src='https://img.icons8.com/ios-filled/50/ffffff/viber.png' width='24' height='24'/>Viber</div></a>")

# Messenger
m_style = "background-color:#0084FF; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; cursor:pointer; box-shadow:0 4px 10px rgba(0,0,
