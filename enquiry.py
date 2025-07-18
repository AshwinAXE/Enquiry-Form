import streamlit as st

# Page Configuration
st.set_page_config(page_title="AXE Health Enquiry", layout="centered")

# Brand emails dictionary
brand_emails = {
    "Farmaforce": "farmaforce@yourdomain.com",
    "PharmaPrograms": "pharmaprograms@yourdomain.com",
    "Precision Health": "precision@yourdomain.com",
    "Wellness": "wellness@yourdomain.com",
    "Sinapse Health": "sinapse@yourdomain.com",
    "Praxhub": "praxhub@yourdomain.com"
}

# Logo (make sure logo.png is in the same folder)
st.image("logo.png", width=140)

# Form header
st.title("Enquire with AXE Health")
st.write("Please select the brand you wish to contact. We'll route your message accordingly.")

# Form component
with st.form("enquiry_form"):
    brand = st.selectbox("Select Brand", [""] + list(brand_emails.keys()))
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send Enquiry")

    if submitted:
        if not brand or not name or not email or not message:
            st.error("Please fill in all fields.")
        else:
            recipient = brand_emails[brand]
            mailto_link = (
                f"mailto:{recipient}"
                f"?subject=AXE Health Enquiry"
                f"&body=Name: {name}%0AEmail: {email}%0AMessage: {message}"
            )
            st.success("Thank you! Click below to send your enquiry.")
            st.markdown(f"[📧 Send Email]({mailto_link})", unsafe_allow_html=True)

