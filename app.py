import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Page Config
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# 2. Styles
st.markdown("""
<style>
#MainMenu,footer,header,[data-testid="stHeader"]{visibility:hidden;display:none;}
.stApp{background-color:#0E1117;color:white;}
.stTextArea textarea{border-radius:15px;background-color:#161B22;color:white;}
</style>
""", unsafe_allow_html=True)

# 3. Time & Logic
now = datetime.now()
ts = now.strftime("%I:%M %p")
st.title("🛡️ SafeCheck")
msg = f"I am okay, safe, and all is good! ❤️\n(Sent at {ts})"
txt = st.text_area("Message:", value=msg, height=140)
p_msg = urllib.parse.quote(txt)

# 4. Building the Grid pieces safely
# CSS bits
b_s = "height:75px;border-radius:18px;display:flex;"
b_s += "align-items:center;justify-content:center;"
b_s += "font-weight:600;font-size:15px;gap:10px;"
b_s += "box-shadow:0 4px 10px rgba(0,0,0,0.3);"

h = []
h.append("<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;'>")

# WhatsApp
w_a = f"<a href='whatsapp://send?text={p_msg}' target='_top' style='text-decoration:none;'>"
h.append(w_a + f"<div style='background-color:#25D366;color:white;{b_s}'>")
h.append("<img src='https://img.icons8.com/material-outlined/48/ffffff/whatsapp.png' width='28'/>WhatsApp</div></a>")

# iMessage
i_m = f"<a href='sms:&body={p_msg}' target='_top' style='text-decoration:none;'>"
h.append(i_m + f"<div style='background-color:#007AFF;color:white;{b_s}'>")
h.append("<img src='https://img.icons8.com/ios-filled/50/ffffff/speech-bubble.png' width='24'/>iMessage</div></a>")

# Viber
v_b = f"<a href='viber://forward?text={p_msg}' target='_top' style='text-decoration:none;'>"
h.append(v_b + f"<div style='background-color:#7360F2;color:white;{b_s}'>")
h.append("<img src='https://img.icons8.com/ios-filled/50/ffffff/viber.png' width='24'/>Viber</div></a>")

# Messenger
m_s = f"background-color:#0084FF;color:white;cursor:pointer;{b_s}"
h.append(f"<div onclick='sh()' style='{m_s}'>")
h.append("<img src='https://img.icons8.com/material-sharp/48/ffffff/facebook-messenger.png' width='26'/>Messenger</div>")

# Others
o_s = f"grid-column:span 2;background-color:#30363D;color:white;cursor:pointer;{b_s}"
h.append(f"<div onclick='sh()' style='{o_s}'>")
h.append("<img src='https://img.icons8.com/ios-glyphs/60/ffffff/external-link.png' width='24'/>Other Apps</div>")

h.append("</div><script>function sh(){if(navigator.share){")
h.append(f"navigator.share({{text:'{txt.replace_newline=' '}'}});")
h.append("}else{alert('Use another app');}}</script>")

# 5. Final Join and Render
st.components.v1.html("".join(h), height=320)
st.caption("Safety Dashboard")
