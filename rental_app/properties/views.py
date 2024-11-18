import streamlit as st
import requests
from django.shortcuts import render, redirect
from .forms import propertyForm

def main():
 def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(); 

            return redirect('property_list')  
    else:
        form = PropertyForm()
    return render(request, 'create_property.html', {'form': form})

def update_property(property_id):
    # Fetch property details from API
    url = f"http://your_api_endpoint/properties/{property_id}"
    response = requests.get(url)
    property_data = response.json()

    # Display property details and update form
    st.title(f"Update Property: {property_data['title']}")

    # Create a form with fields for editing property details
    with st.form(key='update_property_form'):
        title = st.text_input("Title", property_data['title'])
        description = st.text_area("Description", property_data['description'])
        # Add other fields as needed

        if st.form_submit_button("Update Property"):
            # Send updated data to API
            updated_data = {
                "title": title,
                "description": description,
                "location": property_data['location'],
                "price": property_data['price'],
                "image":  property_data['image'],
                "number_of_rooms": property_data['number_of_rooms'],
                 "amenities": property_data['amenities'],
                

            }
            response = requests.put(url, json=updated_data)
            if response.status_code == 200:
                st.success("Property updated successfully!")
            else:
                st.error("Error updating property.")

def list_properties():
    # Fetch property list from API
    url = "http://your_api_endpoint/properties/"
    response = requests.get(url)
    properties = response.json()

# Display other property details
    st.title("Property List")
    for property in properties:
        st.write(f"**{property['title']}**")
        st.write(f"Description: {property['description']}")
        st.write(f"location: {property['location']}")
        st.write(f"price: {property['price']}")
        st.write(f"image: {property['image']}")
        st.write(f"number_of_rooms: {property['number_of_rooms']}")
        st.write(f"amenities: {property['amenities']}")



        

        #  button to update each property
        update_button = st.button("Update", key=property['id'])
        if update_button:
            update_property(property['id'])

       # button to delete each property
        delete_button = st.button("Delete", key=property['id'])
        if delete_button:
            delete_property(property['id'])

if __name__ == "__main__":
    st.title("LeaseLift Property Management")
    # Add navigation or other UI elements

    list_properties()

    def delete_property(property_id):
        
        #... fetch property details from API

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
    location = st.text_area("Location")
    price = st.number_input("Price")
    image = st.file_uploader("Image")
    number_of_rooms = st.number_input("Number of rooms")
    amenities = st.text_area("amenitites")

    

    if st.button("Create Property"):
        data = {
            "name": name,
            "description": description,
            "location": location,
            "price": price,
            "image": image,
            "number_of_rooms": number_of_rooms,
            "amenities": amenities,
          
        }
        response = requests.post("http://your_django_backend_url/properties/", json=data)
        if response.status_code == 201:
            st.success("Property created successfully!")
        else:
            st.error("Error creating property.")




            from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PropertySerializer
from .models import Property

class PropertyListView(APIView):
    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)