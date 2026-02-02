import streamlit as st
import urllib.parse

# 1. Page Configuration & UI Cleanup
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display:none;}
    div.stButton > button:first-child {
        height: 3.5em;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. App Logic
st.title("🛡️ Universal Check-In")

DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"
custom_message = st.text_area("Finalize your message:", value=DEFAULT_MSG, height=120)
encoded_msg = urllib.parse.quote(custom_message)

st.write("### Choose a Chat App:")

# 3. Native Share Script (The Magic for Messenger)
# This JavaScript triggers the phone's actual share menu
share_js = f"""
<script>
function share() {{
    if (navigator.share) {{
        navigator.share({{
            text: `{custom_message}`
        }}).then(() => {{
            console.log('Thanks for sharing');
        }})
        .catch(console.error);
    }} else {{
        alert('Share not supported on this browser');
    }}
}}
</script>
<button onclick="share()" style="
    width: 100%;
    height: 3.5em;
    background-color: #0084FF;
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
">🟦 Messenger / All Apps</button>
"""

# 4. The Layout
col1, col2 = st.columns(2)

with col1:
    # WhatsApp
    st.link_button("🟢 WhatsApp", f"whatsapp://send?text={encoded_msg}", use_container_width=True)
    # Viber
    st.link_button("💜 Viber", f"viber://forward?text={encoded_msg}", use_container_width=True)

with col2:
    # SMS/iMessage
    st.link_button("🔵 iMessage/SMS", f"sms:&body={encoded_msg}", use_container_width=True)
    # Messenger Fallback (The JS Button)
    st.components.v1.html(share_js, height=70)

st.divider()
st.caption("The Blue button triggers your phone's 'Share' menu. Pick Messenger from the list!")
