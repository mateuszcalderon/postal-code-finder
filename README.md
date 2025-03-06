<p align="center">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" height="60" width="60">
</p>

<div align="center">
  <h1>Postal Code Finder</h1>
</div>

Postal Code Finder is a Python-based tool designed to validate, retrieve, and display location details for Canadian Postal Codes and U.S. ZIP Codes. Using the Zippopotam API, it fetches geographic data such as city, state, and coordinates. It also generates interactive maps to visually represent the given location.

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
  def is_postal_code_valid(postal_code, country_code):
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
