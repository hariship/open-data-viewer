import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS

from config.constants import geocoder_api_key

app = Flask(__name__)
CORS(app)

# Wikipedia API endpoint
api_url = "https://en.wikipedia.org/w/api.php"

# OpenCage Geocoder API endpoint
geocoder_api_url = f"https://api.opencagedata.com/geocode/v1/json?key={geocoder_api_key}&pretty=1"

# Cache for population data
population_cache = {}

# Function to extract population count and last updated date for a given country
def get_population_info(country_name):
    # Check if data is in the cache
    country_name_lower = country_name.lower()  # Convert to lowercase
    if country_name_lower in population_cache:
        return population_cache[country_name_lower]

    # Parameters for the API request to fetch the page content
    params = {
        "action": "parse",
        "page": "List_of_countries_and_dependencies_by_population",
        "format": "json"
    }

    # Make the API request to fetch the page content
    response = requests.get(api_url, params=params)
    data = response.json()

    # Check if the request was successful
    if "parse" in data:
        # Extract the HTML content of the page
        html_content = data["parse"]["text"]["*"]

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Find the table containing population data
        population_table = soup.find("table", class_="wikitable")

        if population_table:
            # Extract the population data
            rows = population_table.find_all("tr")
            is_after_india = False  # Flag to check if we are after the "India" row
            india_population = None  # Store the population value for India
            india_last_updated = None  # Store the last updated date for India
            for row in rows:
                columns = row.find_all("td")
                if columns:
                    # Check if the first column contains the country name
                    if is_after_india:
                        country_name = columns[1].get_text().strip()
                    else:
                        country_name = columns[0].get_text().strip()

                    # Handle "India" row separately
                    if not is_after_india:
                        if "India" in country_name:
                            # Set the flag to indicate we are after "India"
                            is_after_india = True
                            # Extract population and last updated for India
                            india_population = columns[1].get_text().strip()
                            india_last_updated = columns[3].get_text().strip()
                        else:
                            # Continue to the next row if it's not India
                            continue

                    # Check if the country name matches the input
                    if country_name.lower() == country_name_lower:
                        # Update population values for India
                        population = india_population if "India" in country_name else columns[2].get_text().strip()
                        last_updated = india_last_updated if "India" in country_name else columns[4].get_text().strip()
                        population_info = {
                            "Country": country_name,
                            "Population": population,
                            "Last_Updated": last_updated
                        }
                        # Cache the data for future requests
                        population_cache[country_name_lower] = population_info
                        return population_info
            # If the country name is not found
            return {"error": "Country not found"}
        else:
            return {"error": "Table not found on the page"}


    else:
        return {"error": "Failed to fetch data from Wikipedia API"}

# Function to get country information based on latitude and longitude
def get_country_info(latitude, longitude):
    try:
        # Send a request to the OpenCage Geocoder API to get country information
        geocoder_response = requests.get(f"{geocoder_api_url}&q={latitude}+{longitude}")
        geocoder_data = geocoder_response.json()

        if "results" in geocoder_data and len(geocoder_data["results"]) > 0:
            result = geocoder_data["results"][0]
            country_name = result.get("components", {}).get("country")
            if country_name:
                # Get population information using the country name
                population_info = get_population_info(country_name)
                return population_info
            else:
                return {"error": "Country not found in geocoder response"}
        else:
            return {"error": "No results found in geocoder response"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/get_population', methods=['GET'])
def get_population():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if not latitude or not longitude:
        return jsonify({"error": "Please provide valid latitude and longitude parameters"})

    # Get country information based on latitude and longitude
    country_info = get_country_info(latitude, longitude)

    return jsonify(country_info)

if __name__ == '__main__':
    app.run()
