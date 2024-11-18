import streamlit as st
import requests  # for API requests

# Assuming you have a Django REST Framework API for property management
API_URL = "http://your_api_endpoint/properties/"  # Replace with your actual API endpoint

def update_property(property_id):
    # Fetch property details from API
    url = f"{API_URL}{property_id}"
    response = requests.get(url)
    property_data = response.json()

    # Create a form for editing property details
    with st.form(key=f"update_property_{property_id}"):
        title = st.text_input("Title", property_data["title"])
        description = st.text_area("Description", property_data["description"])
        # Add other relevant fields like address, rent, etc.

        if st.form_submit_button("Update Property"):
            # Send updated data to API
            updated_data = {
                "title": title,
                "description": description,
                # ... other fields
            }
            response = requests.put(url, json=updated_data)
            if response.status_code == 200:
                st.success("Property updated successfully!")
            else:
                st.error("Error updating property.")


        if __name__ == "__main__":
            st.title("LeaseLift - Property Management")

    # Authentication (Optional): Implement user authentication to restrict access
    # ...

    # List all properties for the authenticated landlord
    response = requests.get(f"{API_URL}?landlord_id={property_id}")  # Replace with your filtering logic
    properties = response.json()

    if properties:
        st.subheader("Your Properties:")
        for property in properties:
            st.write(f"**{property['title']}**")
            st.write(f"Description: {property['description']}")
            # ... show other relevant details

            # Button to update each property
            update_button = st.button("Update", key=property["id"])
            if update_button:
                update_property(property["id"])
    else:
        st.info("You don't have any properties yet.")