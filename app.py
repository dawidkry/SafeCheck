import streamlit as st
import urllib.parse

# 1. Page Configuration
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# 2. CSS Styling Logic
st.markdown("""
    <style>
    /* Hide Streamlit Header/Footer */
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display:none;}
    
    /* Global Button Styles */
    div.stLinkButton > a, div.stButton > button {
        height: 4em !important;
        width: 100% !important;
        border-radius: 12px !important;
        border: none !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        color: white !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
    }

    /* Specific Button Colors */
    /* WhatsApp Green */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) div.stLinkButton > a:first-child {
        background-color: #25D366 !important;
    }
    /* Viber Purple */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) div.stLinkButton > a:last-child {
        background-color: #7360F2 !important;
        margin-top: 10px;
    }
    /* iMessage Blue */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) div.stLinkButton > a:first-child {
        background-color: #007AFF !important;
    }
    
    .stTextArea textarea {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. App Content
st.title("🛡️ SafeCheck")

DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"
custom_message = st.text_area("Edit Message:", value=DEFAULT_MSG, height=120)
encoded_msg = urllib.parse.quote(custom_message)

st.write("### Choose your app:")

# 4. The Grid
col1, col2 = st.columns(2)

with col1:
    st.link_button("🟢 WhatsApp", f"whatsapp://send?text={encoded_msg}", use_container_width=True)
    st.link_button("💜 Viber", f"viber://forward?text={encoded_msg}", use_container_width=True)

with col2:
    st.link_button("🔵 iMessage", f"sms:&body={encoded_msg}", use_container_width=True)
    
    # 5. Messenger / All Apps (Custom

