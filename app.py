import streamlit as st
import urllib.parse

st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# CSS for styling
st.markdown("""<style>div.stButton > button:first-child {height: 3.5em; font-size: 18px; font-weight: bold; border-radius: 10px;}</style>""", unsafe_allow_html=True)

# Config
PHONE_NUMBER = "1234567890" 
FB_USERNAME = "your.username"
DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"

st.title("🛡️ Universal Check-In")
custom_message = st.text_area("Message Preview:", value=DEFAULT_MSG, height=120)
encoded_msg = urllib.parse.quote(custom_message)

st.divider()
st.write("### Send via:")
col1, col2 = st.columns(2)

with col1:
    st.link_button("🟢 WhatsApp", f"https://wa.me/{PHONE_NUMBER}?text={encoded_msg}", use_container_width=True)
    # NEW VIBER LINK
    st.link_button("💜 Viber", f"https://share.viber.com/forward?text={encoded_msg}", use_container_width=True)

with col2:
    # Use ';' for iOS and '?' for Android as a compromise, but '&' usually works for both now
    st.link_button("🔵 iMessage/SMS", f"sms:{PHONE_NUMBER}&body={encoded_msg}", use_container_width=True)
    st.link_button("🟦 Messenger", f"https://m.me/{FB_USERNAME}", use_container_width=True)

st.divider()
if st.button("📋 Copy Message for Messenger", use_container_width=True):
    st.code(custom_message, language=None)
    st.success("Copied!")
