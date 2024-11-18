import streamlit as st
import requests

def create_property():
    st.title("Add a New Property")

    property_name = st.text_input("Property Name")
    property_description = st.text_area("Property Description")
    property_address = st.text_input("Property Address")
    property_price = st.number_input("Property Price")
    property_image = st.file_uploader("Upload Property Image")

    if st.button("Add Property"):
        # Handle form submission here
        # You can send the data to your backend API for processing
        # and storing in the database.

        # Example: Sending data to a hypothetical API endpoint
        data = {
            "name": property_name,
            "description": property_description,
            "address": property_address,
            "price": property_price,
            "image": property_image
        }
        response = requests.post("http://your_api_endpoint", json=data)
        if response.status_code == 201:
            st.success("Property added successfully!")
        else:
            st.error("Error adding property.")

if __name__ == "__main__":
    create_property()