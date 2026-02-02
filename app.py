import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# 2. Hide Streamlit UI Decorations
st.markdown("""
    <style>
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display:none;}
    .stTextArea textarea { 
        border-radius: 15px; 
        border: 2px solid #f0f2f6; 
        padding: 10px;
        font-size: 16px;
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

# 5. The Grid (Updated iMessage to Baby Blue)
html_lines = [
    '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-family: sans-serif;">',
    
    # WhatsApp
    f'<a href="whatsapp://send?text={encoded_msg}" style="text-decoration:none;">',
    '<div style="background-color:#25D366; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">',
    '<img src="https://img.icons8.com/material-outlined/48/ffffff/whatsapp.png" width="28" height="28"/>WhatsApp</div></a>',
    
    # iMessage (BABY BLUE: #89CFF0)
    f'<a href="sms:&body={encoded_msg}" style="text-decoration:none;">',
    '<div style="background-color:#89CFF0; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">',
    '<img src="https://img.icons8.com/ios-filled/50/ffffff/speech-bubble.png" width="24" height="24"/>iMessage</div></a>',
    
    # Viber
    f'<a href="viber://forward?text={encoded_msg}" style="text-decoration:none;">',
    '<div style="background-color:#7360F2; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">',
    '<img src="https://img.icons8.com/ios-filled/50/ffffff/viber.png" width="24" height="24"/>Viber</div></a>',
    
    # Messenger
    '<div onclick="shareNative()" style="background-color:#0084FF; color:white; height:75px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; cursor:pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">',
    '<img src="https://img.icons8.com/material-sharp/48/ffffff/facebook-messenger.png" width="26" height="26"/>Messenger</div>',
    
    '</div>',
    
    '<script>',
    'function shareNative() {',
    '  if (navigator.share) {',
    f'    navigator.share({{ text: "{custom_message}" }});',
    '  } else {',
    '    alert("Sharing not supported");',
    '  }',
    '}',
    '</script>'
]

# Join the list into one big string
html_final = "".join(html_lines)

# Render the grid
st.components.v1.html(html_final, height=200)

st.divider()
st.caption("Official Safety Dashboard")
