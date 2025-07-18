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

# Title and instructions
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
            subject = "AXE Health Enquiry"
            body = f"Name: {name}%0AEmail: {email}%0AMessage: {message}"
            mailto_link = f"mailto:{recipient}?subject={subject}&body={body}"

            st.success("Thanks! Click the button below to open your email client.")
            st.markdown(
                f'<a href="{mailto_link}"><button style="background-color:#0073e6;color:white;padding:10px 20px;border:none;border-radius:5px;">📧 Send via Email</button></a>',
                unsafe_allow_html=True
            )


