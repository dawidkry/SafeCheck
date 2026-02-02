import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Configuration
st.set_page_config(page_title="SafeCheck", layout="centered")

# 2. Styles (Restoring the Pro Font)
st.markdown("<style>#MainMenu,footer,header{display:none;}"
".stApp{background-color:#0E1117;color:white;font-family:-apple-system,"
"BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;}"
".stTextArea textarea{border-radius:15px;font-family:inherit;"
"background-color:#161B22;color:white;border:2px solid #30363D;}</style>", 
unsafe_allow_html=True)

# 3. Content
now = datetime.now()
ts = now.strftime("%I:%M %p")
st.title("🛡️ SafeCheck")
msg = "I am okay, safe, and all is good! ❤️\n(%s)" % ts
txt = st.text_area("Message:", value=msg, height=140)
p_msg = urllib.parse.quote(txt)

# 4. Icon Links
B = "https://img.icons8.com/"
W_I = B + "material-outlined/48/ffffff/whatsapp.png"
I_I = B + "ios-filled/50/ffffff/speech-bubble.png"
V_I = B + "ios-filled/50/ffffff/viber.png"
M_I = B + "material-sharp/48/ffffff/facebook-messenger.png"
O_I = B + "ios-glyphs/60/ffffff/external-link.png"

# 5. Button Style (Restored Font & Tap Effect)
S = "height:75px;border-radius:18px;display:flex;"
S += "align-items:center;justify-content:center;"
S += "font-weight:600;font-size:15px;gap:10px;"
S += "box-shadow:0 4px 10px rgba(0,0,0,0.3);font-family:inherit;"

# 6. Grid Construction
h = []
h.append("<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;'>")

# WhatsApp
h.append("<a href='whatsapp://send?text=%s' target='_top' style='text-decoration:none;'>" % p_msg)
h.append("<div style='background-color:#25D366;color:white;%s'>" % S)
h.append("<img src='%s' width='28'/>WhatsApp</div></a>" % W_I)

# iMessage
h.append("<a href='sms:&body=%s' target='_top' style='text-decoration:none;'>" % p_msg)
h.append("<div style='background-color:#007AFF;color:white;%s'>" % S)
h.append("<img src='%s' width='24'/>iMessage</div></a>" % I_I)

# Viber
h.append("<a href='viber://forward?text=%s' target='_top' style='text-decoration:none;'>" % p_msg)
h.append("<div style='background-color:#7360F2;color:white;%s'>" % S)
h.append("<img src='%s' width='24'/>Viber</div></a>" % V_I)

# Messenger
h.append("<div onclick='sh()' style='background-color:#0084FF;color:white;cursor:pointer;%s'>" % S)
h.append("<img src='%s' width='26'/>Messenger</div>" % M_I)

# Others
h.append("<div onclick='sh()' style='grid-column:span 2;background-color:#30363D;color:white;cursor:pointer;%s'>" % S)
h.append("<img src='%s' width='24'/>Other Apps</div>" % O_I)

# JS
cl = txt.replace("\n", " ")
h.append("</div><script>function sh(){if(navigator.share){")
h.append("navigator.share({text:'%s'});" % cl)
h.append("}else{alert('Try another app');}}</script>")

st.components.v1.html("".join(h), height=320)
st.caption("Official Safety Dashboard")
