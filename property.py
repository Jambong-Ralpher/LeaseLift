import streamlit as st
import requests
def main():
  def create_property():
     # ... handle form submission and send data to the API

    def update_property(property_id):
    # ... fetch property details, display form, and send updated data to API

      def delete_property(property_id):
    # ... send a DELETE request to the API endpoint

# ... other functions for listing properties, searching, etc.

      
        st.title("Property Management")
     # ... display options for creating, updating, and deleting properties
    # ... call the respective functions based on user input

if __name__ == "__main__":
 main()


 def create_property():
    name = st.text_input("Name")
    description = st.text_area("Description")
    # ... other fields

    if st.button("Create Property"):
        data = {
            "name": name,
            "description": description,
            # ... other fields
        }
        response = requests.post("http://your_django_backend_url/properties/", json=data)
        if response.status_code == 201:
            st.success("Property created successfully!")
        else:
            st.error("Error creating property.")