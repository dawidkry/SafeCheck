import streamlit as st
import urllib.parse

# 1. Page Configuration
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# 2. Hide Streamlit UI
st.markdown("""
    <style>
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display:none;}
    .stTextArea textarea { border-radius: 15px; border: 1px solid #ddd; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. App Content
st.title("🛡️ SafeCheck")

DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"
custom_message = st.text_area("Edit Message:", value=DEFAULT_MSG, height=120)
encoded_msg = urllib.parse.quote(custom_message)

st.write("### Choose your app:")

# 4. The Custom Button Grid with Official Logos
# Using SimpleIcons CDN for official brand marks
grid_html = f"""
<div style="
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
">
    <a href="whatsapp://send?text={encoded_msg}" style="text-decoration:none;">
        <div style="background-color:#25D366; color:white; height:70px; border-radius:15px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px;">
            <img src="https://cdn.simpleicons.org/whatsapp/white" width="24" height="24" />
            WhatsApp
        </div>
    </a>

    <a href="sms:&body={encoded_msg}" style="text-decoration:none;">
        <div style="background-color:#000000; color:white; height:70px; border-radius:15px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px;">
            <img src="https://cdn.simpleicons.org/apple/white" width="24" height="24" />
            iMessage
        </div>
    </a>

    <a href="viber://forward?text={encoded_msg}" style="text-decoration:none;">
        <div style="background-color:#7360F2; color:white; height:70px; border-radius:15px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px;">
            <img src="https://cdn.simpleicons.org/viber/white" width="24" height="24" />
            Viber
        </div>
    </a>

    <div onclick="shareNative()" style="background-color:#0084FF; color:white; height:70px; border-radius:15px; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:15px; gap:10px; cursor:pointer;">
        <img src="https://cdn.simpleicons.org/facebookmessenger/white" width="24" height="24" />
        Messenger
    </div>
</div>

<script>
function shareNative() {{
    if (navigator.share) {{
        navigator.share({{ text: `{custom_message}` }});
    }} else {{
        alert('Sharing not supported on this browser.');
    }}
}}
</script>
"""

# Render the grid
st.components.v1.html(grid_html, height=180)

st.divider()
st.caption("Official Safety Dashboard • Pick a contact to send.")
