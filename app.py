import streamlit as st

# Initialize a dictionary to store user data
user_data = {}

# Sidebar for navigation
st.sidebar.title("Repair Management System")
option = st.sidebar.selectbox("Choose an option", ["Upload for Repair", "Report Fix"])

if option == "Upload for Repair":
    st.title("Upload for Repair")
    
    # User input for name
    name = st.text_input("Enter your name:")
    
    # File uploader for photo
    photo = st.file_uploader("Upload a photo of the repair facility", type=["jpg", "jpeg", "png"])
    
    # Input for naming the photo
    photo_name = st.text_input("Name your photo:")
    
    if st.button("Submit"):
        if name and photo and photo_name:
            # Store the uploaded photo and associated data
            user_data[name] = {"photo": photo, "photo_name": photo_name}
            st.success("Photo uploaded successfully!")
        else:
            st.error("Please fill in all fields.")

elif option == "Report Fix":
    st.title("Report Fix")
    
    # Select a name from the uploaded data
    if user_data:
        name = st.selectbox("Select your name:", list(user_data.keys()))
        
        if name:
            st.write(f"Uploaded Photo: {user_data[name]['photo_name']}")
            if st.button("Mark as Fixed"):
                st.success(f"The photo '{user_data[name]['photo_name']}' has been marked as fixed.")
    else:
        st.warning("No uploaded photos available. Please upload a photo first.")
