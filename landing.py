import streamlit as st
from PIL import Image
import webbrowser

# Load the logo
logo = Image.open("ipams_logo(1).png")

# Display the logo in the top-left corner using custom CSS
st.markdown(
    """
    <style>
    .fixed-logo {
        position: fixed;
        top: 10px;
        left: 10px;
        width: 30px;
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display logo
st.image(logo, use_column_width=False, width=50, output_format="PNG")

# Set up session state to handle page transitions
if "page" not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

# Page 1: Welcome
if st.session_state.page == 1:
    st.title("Welcome to IPAMS")
    st.write("Click 'Next' to proceed to the Terms and Conditions.")
    if st.button("Next"):
        next_page()

# Page 2: Terms and Conditions
elif st.session_state.page == 2:
    st.title("Terms and Conditions")
    st.write("Please read and accept the following terms and conditions to proceed.")

    # Sample Terms and Conditions text
    terms_text = """
    **IPAMS Terms and Conditions**

    1. **Acceptance of Terms**  
       By accessing and using the IPAMS platform, you agree to comply with and be bound by the following terms and conditions. Please review them carefully.

    2. **Eligibility**  
       You must be at least 18 years old to use the platform. By using this service, you represent and warrant that you meet all eligibility requirements.

    3. **Use of the Platform**  
       You agree to use IPAMS solely for lawful purposes. You are responsible for ensuring that your use complies with all applicable local, state, and federal laws.

    4. **Intellectual Property**  
       All content, features, and functionality on the IPAMS platform are and will remain the exclusive property of the IPAMS development team.

    5. **Data Collection and Privacy**  
       By using the platform, you consent to the collection and use of your personal information in accordance with our Privacy Policy.

    6. **User-Provided Content**  
       You may upload personal information, including images and identification documents. By uploading this content, you grant IPAMS permission to use this content in accordance with the platform’s purpose and our Privacy Policy.

    7. **Disclaimer of Warranties**  
       The IPAMS platform is provided on an "as is" basis. We make no warranties or representations about the accuracy, reliability, or completeness of the platform’s content.

    8. **Limitation of Liability**  
       Under no circumstances shall IPAMS or its affiliates be liable for any indirect, incidental, or consequential damages resulting from the use of the platform.

    9. **Changes to Terms**  
       IPAMS reserves the right to modify these terms at any time. Continued use of the platform after any changes constitutes acceptance of the new terms.

    10. **Contact Us**  
        For questions regarding these terms, please contact IPAMS support.

    By clicking "Next," you agree to abide by these Terms and Conditions.
    """
    st.write(terms_text)

    # Agreement checkbox
    agree = st.checkbox("I agree to the Terms and Conditions", key="terms")
    if st.button("Next") and agree:
        next_page()
    elif st.button("Next"):
        st.warning("Please agree to the Terms and Conditions to proceed.")

# Page 3: Upload Details
elif st.session_state.page == 3:
    st.title("Upload Your Details")
    full_name = st.text_input("Full Name")
    phone_number = st.text_input("Phone Number")
    id_card = st.file_uploader("Upload ID Card", type=["png", "jpg", "jpeg", "pdf"])
    photo = st.file_uploader("Upload Photo", type=["png", "jpg", "jpeg"])
    
    # Check if all required fields are filled
    if st.button("Next"):
        if full_name and phone_number and id_card is not None and photo is not None:
            next_page()
        else:
            st.warning("Please complete all fields to proceed.")

# Page 4: Redirect to project page
elif st.session_state.page == 4:
    st.write("Thank you! You will now be redirected to the project page.")
    # Redirect to the specified URL
    project_url = "https://project9wgrvmfprfmzhswjtdwio6.streamlit.app/"
    webbrowser.open_new_tab(project_url)
    st.write(f"If you are not redirected automatically, click [here]({project_url}).")
