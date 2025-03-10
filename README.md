<p align="center">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" height="60" width="60">
</p>

<div align="center">
  <h1>Postal Code Finder</h1>
</div>

Postal Code Finder is a Python-based tool designed to validate, retrieve, and display location details for Canadian Postal Codes and U.S. ZIP Codes. Using the Zippopotam API, it fetches geographic data such as the place name, state, country and coordinates. It also generates interactive maps to visually represent the given location.

## Code Walkthrough:
#### Library:
```python
  import requests
  import re
  import folium
```

  - ` requests `: Handles HTTP requests to interact with the Zippopotam API.
  - ` re `: Provides regular expressions for validating Postal/ZIP Code formats.
  - ` folium `: Generates interactive maps.

#### is_postal_code_valid Function:
```python
  def is_postal_code_valid(country_code, postal_code):
    canada_pattern = re.compile(r"^[A-Za-z]\d[A-Za-z]$")
    us_pattern = re.compile(r"^\d{5}(-\d{4})?$")
    if country_code == "ca":
        return bool(canada_pattern.match(postal_code))
    elif country_code == "us":
        return bool(us_pattern.match(postal_code))
    else:
        return False
```

  - This function ensures the Postal/ZIP Code follows the standard format for Canada or the United States.
  - Valid formats:
    - Canada (e.g., V6T): Matches the Regex Pattern ` ^[A-Za-z]\d[A-Za-z]$ `.
    - United States (e.g., 02139): Matches ` ^\d{5}$ `.
  - ` ^[A-Za-z]\d[A-Za-z]$ ` Regex Pattern:
    - ` ^ `: Ensures the Postal/ZIP Code must start at the beginning of the input.
    - ` [A-Za-z] `: Matches a single alphabetic character (uppercase ` A-Z ` or lowercase ` a-z `).
    - ` \d `: Matches a numeric digit (0-9).
    - ` [A-Za-z] `: Matches another single alphabetic character.
    - ` $ `: Ensures it must end exactly where the pattern stops.
  - ` ^\d{5}$ ` Regex Pattern:
    - ` ^ `: Ensures the Postal/ZIP Code must start at the beginning of the input.
    - ` \d `: Matches any numeric digit (0-9).
    - ` {5} `: Specifies that exactly five numeric digits must follow.
    - ` $ `: Ensures it must end exactly where the pattern stops.
  - After that, the ` is_postal_code_valid ` function returns ` True ` or ` False ` based on the input and country code.

#### def get_postal_code_info Function:
```python
  def get_postal_code_info(country_code, postal_code):
    url = f"http://api.zippopotam.us/{country_code}/{postal_code}"
    response = requests.get(url)
    if response.status_code == 200:
        postal_code_data = response.json()
        return postal_code_data
    else:
        return None
```

  - This function constructs the URL dynamically using the ` country_code ` and ` postal_code ` inputs (e.g., ` http://api.zippopotam.us/us/02139 `).
  - Makes a GET request using the ` requests ` library.
  - If the API response is successful (` status_code == 200 `), the data is returned in JSON format. If not, ` None ` is returned.

#### display_selected_info Function:
```python
      if postal_code_info:
        place = postal_code_info["places"][0]
        print(f"Place Name: {place['place name']}")
        print(f"State: {place['state']}, {place['state abbreviation']}")
        print(f"Country: {postal_code_info['country']}, {postal_code_info['country abbreviation']}")
        print(f"Latitude: {place['latitude']}")
        print(f"Longitude: {place['longitude']}")
    else:
        print("Location Not Found.")
```

  - The ` display_selected_info ` function extracts and displays useful location details from the data returned by the API.
  - It accesses the first entry in the "places" array of the API response to gather specific details like the place name, state and state abbreviation, country and country abbreviation and latitude and longitude.

#### generate_map Function:
```python
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
```

  - This function creates an interactive map highlighting the location of the given Postal/ZIP Code.
  - It extracts latitude and longitude from the API response.
  - The Folium library is used to create a map centered on the extracted coordinates. And the ` zoom_start=12 ` parameter defines the initial zoom level of the map, with 12 providing a moderately close view.
  - A marker is placed on the map at the exactly coordinates location and the ` popup ` parameter adds a message displaying the Postal Code that appears when the user clicks on the marker.
  - And then, the function saves the map as an HTML file named after the Postal Code (e.g., ` 02139_MAP.html `).
