import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# 2. Permanent Dark Mode & Button Styling
st.markdown("""
    <style>
    /* Hide Streamlit UI Decorations */
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display:none;}
    
    /* Force Background Color */
    .stApp { background-color: #0E1117; color: #FFFFFF; }

    /* Style the Text Area */
    .stTextArea textarea { 
        border-radius: 15px; border: 2px solid #30363D; 
        background-color: #161B22 !important; color: white !important;
    }

    /* THE FIX: Universal Button Styling */
    /* This makes every link button look like our previous boxes */
    div.stLinkButton > a, div.stButton > button {
        height: 75px !important;
        width: 100% !important;
        border-radius: 18px !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        color: white !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
        transition: transform 0.1s !important;
    }
    div.stLinkButton > a:active { transform: scale(0.98); }

    /* Brand Specific Colors */
    /* WhatsApp */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) div:nth-child(1) a { background-color: #25D366 !important; }
    /* Viber */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) div:nth-child(2) a { background-color: #7360F2 !important; }
    /* iMessage */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) div:nth-child(1) a { background-color: #007AFF !important; }
    /* Messenger/Share */
    div[data-testid="stVerticalBlock"] > div:nth-child(5) button { background-color: #0084FF !important; }
    /* Others */
    div[data-testid="stVerticalBlock"] > div:nth-child(6) button { background-color: #30363D !important; }

    h1, h3 { color: white !important; }
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

# 5. The Native Grid
col1, col2 = st.columns(2)

with col1:
    st.link_button("🟢 WhatsApp", f"whatsapp://send?text={encoded_msg}", use_container_width=True)
    st.link_button("💜 Viber", f"viber://forward?text={encoded_msg}", use_container_width=True)

with col2:
    st.link_button("🔵 iMessage", f"sms:&body={encoded_msg}", use_container_width=True)
    
    # Messenger "Share" functionality
    # Using a native button to trigger a browser share is more reliable
    if st.button("🟦 Messenger", use_container_width=True):
        st.components.v1.html(f"""
            <script>
            if (navigator.share) {{
                navigator.share({{ text: "{custom_message}" }});
            }} else {{
                alert("Please copy/paste or use a different app.");
            }}
            </script>
        """, height=0)

# Full width "Other" button
if st.button("🔗 Other Apps", use_container_width=True):
    st.components.v1.html(f"""
        <script>
        navigator.share({{ text: "{custom_message}" }});
        </script>
    """, height=0)

st.divider()
st.caption("Official Safety Dashboard • Reliable Link Mode")
