import streamlit as st
import urllib.parse

# 1. Page Configuration for Mobile
st.set_page_config(
    page_title="SafeCheck",
    page_icon="🛡️",
    layout="centered"
)

# Custom CSS for larger, touch-friendly buttons
st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 3.5em;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>""", unsafe_allow_html=True)

# 2. Configuration Variables (Update these!)
PHONE_NUMBER = "1234567890"  # Format: CountryCode + Number (e.g., 447123456789)
FB_USERNAME = "your.fb.username" # Your contact's FB username
DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"

st.title("🛡️ Universal Check-In")

# 3. Message Customization
st.subheader("Message Preview")
custom_message = st.text_area("You can edit this before sending:", value=DEFAULT_MSG, height=120)
encoded_msg = urllib.parse.quote(custom_message)

st.divider()

# 4. Action Buttons
st.write("### Send via:")

# Layout for a 2x2 grid on mobile
col1, col2 = st.columns(2)

with col1:
    # WhatsApp - Pre-fills text & recipient
    wa_url = f"https://wa.me/{PHONE_NUMBER}?text={encoded_msg}"
    st.link_button("🟢 WhatsApp", wa_url, use_container_width=True)

    # Viber - Uses 'forward' to reliably pre-fill text
    viber_url = f"viber://forward?text={encoded_msg}"
    st.link_button("💜 Viber", viber_url, use_container_width=True)

with col2:
    # iMessage / SMS - Pre-fills text & recipient
    # Note: iOS uses '&', Android often uses '?' or ';'
    sms_url = f"sms:{PHONE_NUMBER}&body={encoded_msg}"
    st.link_button("🔵 iMessage/SMS", sms_url, use_container_width=True)

    # Messenger - Opens chat window only (Manual paste required)
    fb_url = f"https://m.me/{FB_USERNAME}"
    st.link_button("🟦 Messenger", fb_url, use_container_width=True)

# 5. Messenger Helper (Copy Button)
st.divider()
st.info("💡 **Tip for Messenger:** Facebook doesn't allow auto-filling text. Click the button below to copy your message before opening Messenger.")

if st.button("📋 Copy Message for Messenger", use_container_width=True
