import requests
import re
import folium

# Function to validate Postal/ZIP Code format.
def is_postal_code_valid(country_code, postal_code):
    canada_pattern = re.compile(r"^[A-Za-z]\d[A-Za-z]$")
    us_pattern = re.compile(r"^\d{5}$")
    if country_code == "ca":
        return bool(canada_pattern.match(postal_code))
    elif country_code == "us":
        return bool(us_pattern.match(postal_code))
    else:
        return False

# Function to get Postal/ZIP Code information from the Zippopotam API.
def get_postal_code_info(country_code, postal_code):
    url = f"http://api.zippopotam.us/{country_code}/{postal_code}"
    response = requests.get(url)
    if response.status_code == 200:
        postal_code_data = response.json()
        return postal_code_data
    else:
        return None

# Function to display selected information about the Postal/ZIP Code.
def display_selected_info(postal_code_info):
    if postal_code_info:
        place = postal_code_info["places"][0]
        print(f"Place Name: {place['place name']}")
        print(f"State: {place['state']}, {place['state abbreviation']}")
        print(f"Country: {postal_code_info['country']}, {postal_code_info['country abbreviation']}")
        print(f"Latitude: {place['latitude']}")
        print(f"Longitude: {place['longitude']}")
    else:
        print("Location Not Found.")

# Function to generate a map of the Postal/ZIP Code location.
def generate_map(postal_code_info):
    if postal_code_info:
        place = postal_code_info["places"][0]
        latitude = float(place["latitude"])
        longitude = float(place["longitude"])
        map = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker(
            [latitude, longitude],
            popup=f"Postal Code: {postal_code_info['post code']}"
        ).add_to(map)
        file_name = f"{postal_code_info['post code']}_MAP.html"
        map.save(file_name)
        print(f"Map Generated and Saved as '{file_name}'.")
    else:
        print("Location Not Found.")

# Main code to input Country and Postal/ZIP Code.
country_code = input("Enter a Country Code (CA or US): ").lower()
if country_code == "ca":
    postal_code = input("Enter Postal Code: ")
elif country_code == "us":
    postal_code = input("Enter ZIP Code: ")
else:
    print("Invalid Country Code.")
    postal_code = None

# Validate and process the Postal/ZIP Code.
if postal_code and is_postal_code_valid(country_code, postal_code):
    info = get_postal_code_info(country_code, postal_code)
    if info:
        display_selected_info(info)
        generate_map(info)
    else:
        print("Valid Format but Data Not Found.")
else:
    if postal_code:
        print("Invalid ZIP/Postal Code Format.")
