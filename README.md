# SafeCheck 🛡️

A simple, Python-powered web application designed for one-tap safety check-ins with family.

## Features
- **One-Tap Messaging:** Pre-fills messages for WhatsApp or SMS/iMessage.
- **On-the-fly Edits:** Modify your status message right before sending.
- **Cross-Platform:** Works on any device with a browser (iOS/Android).

## How to use on Mobile
To make this feel like a native app:
1. Open the deployed Streamlit URL in your mobile browser.
2. **iOS (Safari):** Tap the 'Share' icon -> 'Add to Home Screen'.
3. **Android (Chrome):** Tap the three dots -> 'Install App' or 'Add to Home Screen'.

## Setup
1. Clone this repo.
2. Install requirements: `pip install streamlit`.
3. Run locally: `streamlit run app.py`.


# SafeCheck Plus 🛡️

## Setup Requirements
To make the buttons work, update the following in `app.py`:

1. **Phone Number:** Use international format without the `+` (e.g., `447123456789`).
2. **FB Username:** - Go to your Facebook Profile.
   - Look at the URL: `facebook.com/your.username`. 
   - Copy that username into the `FB_USERNAME` variable.

## Platform Behavior
- **WhatsApp/SMS:** Fully pre-fills the message.
- **Viber:** Opens the chat (behavior varies by device).
- **Messenger:** Opens the direct chat, but you must paste the message (Facebook's privacy limit).

---
*Copyright (c) 2026 dawidkry - All Rights Reserved*
