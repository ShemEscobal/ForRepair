import streamlit as st
import os
import pandas as pd

# Initialize a dictionary to store user data
user_data = {}

# Create a directory for storing uploaded photos
photo_storage_dir = "uploaded_photos"
os.makedirs(photo_storage_dir, exist_ok=True)

# Create or load the Excel file for storing data
excel_file = "repair_data.xlsx"
if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=["Name", "Photo Name", "Status"])
    df.to_excel(excel_file, index=False)

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
            # Save the uploaded photo to the designated directory
            photo_path = os.path.join(photo_storage_dir, photo_name)
            with open(photo_path, "wb") as f:
                f.write(photo.getbuffer())
            
            # Store the uploaded photo and associated data
            user_data[name] = {"photo": photo_path, "photo_name": photo_name, "status": "unfixed"}
            
            # Update the Excel file
            df = pd.read_excel(excel_file)
            df = df.append({"Name": name, "Photo Name": photo_name, "Status": "unfixed"}, ignore_index=True)
            df.to_excel(excel_file, index=False)
            
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
                user_data[name]["status"] = "fixed"
                st.success(f"The photo '{user_data[name]['photo_name']}' has been marked as fixed.")
                
                # Update the Excel file
                df = pd.read_excel(excel_file)
                df.loc[df['Name'] == name, 'Status'] = "fixed"
                df.to_excel(excel_file, index=False)
                
                # Calculate and display percentages
                total_photos = len(df)
                fixed_photos = len(df[df['Status'] == "fixed"])
                unfixed_photos = total_photos - fixed_photos
                st.write(f"Percentage Fixed: {fixed_photos / total_photos * 100:.2f}%")
                st.write(f"Percentage Unfixed: {unfixed_photos / total_photos * 100:.2f}%")
    else:
        st.warning("No uploaded photos available. Please upload a photo first.")
