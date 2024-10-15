import streamlit as st

# Set the page title and layout for a user-friendly design
st.set_page_config(page_title="Partner Information Form", layout="centered")

# Add a title to the UI
st.title("Partner Information Form")
st.markdown("Please fill out the required details in the form below:")

# Create a form container to capture partner information
with st.form(key="partnerInformationForm"):  # camelCase for the form key

    # Partner Details Section
    st.subheader("Partner Details")
    partnerId = st.text_input("Partner ID *", placeholder="Enter Partner ID", key="partnerId")  # camelCase variable
    sourcePartnerId = st.text_input("Source Partner ID", placeholder="Enter Source Partner ID", key="sourcePartnerId")  # camelCase variable
    
    # Name Details Section
    name = st.text_input("Name *", placeholder="Enter Full Name", key="name")  # Required field with a clear placeholder
    legalName = st.text_input("Legal Name", placeholder="Enter Legal Name", key="legalName")  # camelCase variable

    # Address Section
    st.subheader("Address Details")
    address1 = st.text_input("Address 1", placeholder="Enter Address 1", key="address1")  # camelCase variable
    address2 = st.text_input("Address 2", placeholder="Enter Address 2 (optional)", key="address2")  # camelCase variable
    address3 = st.text_input("Address 3", placeholder="Enter Address 3 (optional)", key="address3")  # camelCase variable
    address4 = st.text_input("Address 4", placeholder="Enter Address 4 (optional)", key="address4")  # camelCase variable
    
    # City and State fields
    city = st.text_input("City", placeholder="Enter City", key="city")  # camelCase variable
    state = st.text_input("State", placeholder="Enter State", key="state")  # camelCase variable

    # Country Dropdown Menu
    country = st.selectbox(
        "Country *", 
        ["Select Country", "United Kingdom", "United States", "Canada", "India", "Australia", "Others"],
        index=0,
        key="country"
    )

    # Submit button for form submission
    submitButton = st.form_submit_button(label="Submit")  # camelCase for the button variable

# Handling form submission
if submitButton:
    # Checking if all required fields are filled
    if partnerId and name and country != "Select Country":
        st.success("Form Submitted Successfully!")
        st.write("### Partner Details Summary:")
        st.write(f"**Partner ID**: {partnerId}")
        st.write(f"**Source Partner ID**: {sourcePartnerId}")
        st.write(f"**Name**: {name}")
        st.write(f"**Legal Name**: {legalName}")
        
        st.write("### Address Information:")
        st.write(f"**Address 1**: {address1}")
        st.write(f"**Address 2**: {address2}")
        st.write(f"**Address 3**: {address3}")
        st.write(f"**Address 4**: {address4}")
        st.write(f"**City**: {city}")
        st.write(f"**State**: {state}")
        st.write(f"**Country**: {country}")
    else:
        st.error("Please fill out all required fields marked with an asterisk (*) before submitting.")

# Custom styling for improved appearance
st.markdown(
    """
    <style>
    /* Adjust text input fields and alignment */
    .stTextInput div { margin-top: 5px; }
    .stTextInput input { font-size: 14px; }

    /* Header styling */
    .stHeader, .stSubheader { margin-top: 15px; color: #2E7D32; }

    /* Adjust spacing for the select box */
    .stSelectbox div { margin-bottom: 15px; }

    /* Center the form layout */
    .stApp { text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar information for guidelines
st.sidebar.info("Please ensure that all required fields marked with * are filled before submitting.")

