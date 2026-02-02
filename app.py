import streamlit as st
import urllib.parse

# 1. Page Configuration
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# Hide Streamlit UI Elements
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stHeader"] {display:none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Button Styling
st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 3.5em;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    </style>""", unsafe_allow_html=True)

# 2. App Content
st.title("🛡️ Universal Check-In")

DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"
custom_message = st.text_area("Finalize your message:", value=DEFAULT_MSG, height=120)
encoded_msg = urllib.parse.quote(custom_message)

st.write("### Choose a Chat App:")

# 3. Share Links Logic
# WhatsApp: No phone number = opens contact selector
wa_share = f"whatsapp://send?text={encoded_msg}"

# Viber: The 'Forward' style you liked
viber_share = f"viber://forward?text={encoded_msg}"

# SMS: No phone number = opens new message screen
sms_share = f"sms:&body={encoded_msg}"

# Messenger: Standard share link (requires manual contact selection)
fb_share = f"https://www.facebook.com/dialog/send?link=https://google.com&app_id=123456789&redirect_uri=https://google.com"

# 4. The Grid
col1, col2 = st.columns(2)

with col1:
    st.link_button("🟢 WhatsApp", wa_share, use_container_width=True)
    st.link_button("💜 Viber", viber_share, use_container_width=True)

with col2:
    st.link_button("🔵 iMessage/SMS", sms_share, use_container_width=True)
    # Using the copy method for Messenger as it is the most reliable
    if st.button("🟦 Messenger (Copy)", use_container_width=True):
        st.code(custom_message, language=None)
        st.info("Now open Messenger and paste.")

st.divider()
st.caption("Tap an app, choose your contact, and hit send.")
