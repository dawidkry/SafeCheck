import streamlit as st
import urllib.parse

st.set_page_config(page_title="SafeCheck Plus", page_icon="🛡️")

# --- CONFIGURATION ---
# Replace these with your real details
PHONE_NUMBER = "1234567890"  # Format: CountryCode + Number (No + sign)
FB_USERNAME = "your.fb.username"  # Find this in your FB Profile settings
DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"

st.title("🛡️ Universal Check-In")

# 1. Last-second customization
custom_message = st.text_area("Edit your status:", value=DEFAULT_MSG, height=100)
encoded_msg = urllib.parse.quote(custom_message)

st.subheader("Send via:")

# Create a grid for the buttons
col1, col2 = st.columns(2)

with col1:
    # WhatsApp (Best support for pre-filled text)
    wa_url = f"https://wa.me/{PHONE_NUMBER}?text={encoded_msg}"
    st.link_button("🟢 WhatsApp", wa_url, use_container_width=True)

    # Viber (Opens chat; pre-fill depends on OS version)
    viber_url = f"viber://chat?number={PHONE_NUMBER}&draft={encoded_msg}"
    st.link_button("💜 Viber", viber_url, use_container_width=True)

with col2:
    # iMessage / SMS
    sms_url = f"sms:{PHONE_NUMBER}&body={encoded_msg}"
    st.link_button("🔵 iMessage/SMS", sms_url, use_container_width=True)

    # Facebook Messenger (Opens chat only)
    fb_url = f"https://m.me/{FB_USERNAME}"
    st.link_button("🟦 Messenger", fb_url, use_container_width=True)

st.divider()
if st.button("📋 Copy Message to Clipboard"):
    # This is a fallback since Messenger won't pre-fill
    st.write(f"Copy this: `{custom_message}`")
    st.success("Now you can paste it into Messenger!")
