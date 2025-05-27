import streamlit as st
import re
import requests
from datetime import datetime

# Page config
st.set_page_config(page_title="Contact Us", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>📬 Contact & Feedback</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Got a thought, bug, or love letter? Drop it below!</p>", unsafe_allow_html=True)
st.markdown("---")

# Contact form
with st.form("contact_form"):
    name = st.text_input("🧑 Your Name")
    email = st.text_input("📧 Gmail (required)")
    message = st.text_area("💬 Your Message or Feedback", height=150)
    submitted = st.form_submit_button("Send")

    if submitted:
        if not re.match(r"^[\w\.-]+@gmail\.com$", email):
            st.error("Please enter a valid Gmail address.")
        elif name.strip() == "" or message.strip() == "":
            st.error("Name and message cannot be empty.")
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payload = {
                "name": name,
                "email": email,
                "message": message,
                "timestamp": timestamp
            }

            # Replace with your Google Apps Script Web App URL
            url = "https://script.google.com/macros/s/AKfycbwIY1tG3T7Xx91O2UOPTZjszj7Z_Y-zGXQ4G-fCpjnuYCX0_uKFnyyyE5KHj99yTdax/exec"

            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    st.success("✅ Feedback submitted! Thanks for reaching out.")
                else:
                    st.error("❌ Failed to submit feedback. Please try again.")
            except Exception as e:
                st.error(f"⚠️ Error: {e}")

# Divider
st.markdown("---")

# Footer with links
st.markdown("""
<div style='text-align: center;'>
    <a href="https://github.com/Arhamhir" target="_blank">🌐 GitHub</a> |
    <a href="https://www.linkedin.com/in/arham-tahir-95626a28a/" target="_blank">🔗 LinkedIn</a>
</div>
<br>
<p style='text-align: center;'>Project by <strong>Syed Ashtar Ali Zaidi</strong> & <strong>Muhammad Arham Tahir</strong></p>
""", unsafe_allow_html=True)
