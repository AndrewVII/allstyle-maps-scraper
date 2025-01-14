import csv
import json
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()


def get_nearyby_place_info(search_query, max_results=20):
    api_key = os.getenv("GOOGLE_API_KEY")
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={search_query}&key={api_key}"

    showrooms = []
    while len(showrooms) < max_results:
        response = requests.get(url)
        results = response.json().get("results", [])
        showrooms.extend(results)

        # Check if there's a next page token
        next_page_token = response.json().get("next_page_token")
        if not next_page_token:
            break  # No more pages available

        # Wait for a short period before making the next request
        time.sleep(
            2
        )  # Google recommends a short delay before using the next_page_token

        # Update the URL with the next page token
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={api_key}"

    # Process the results to get detailed information
    detailed_showrooms = []
    for result in showrooms[:max_results]:  # Limit to 20 results
        place_id = result.get("place_id")
        details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
        details_response = requests.get(details_url)
        details_result = details_response.json().get("result", {})

        showroom = {
            "name": result.get("name"),
            "address": result.get("formatted_address"),
            "phone": details_result.get("formatted_phone_number", "N/A"),
            "website": details_result.get("website", "N/A"),
        }
        detailed_showrooms.append(showroom)

    csv_file = "showrooms.csv"
    csv_columns = ["name", "address", "phone", "website"]

    try:
        with open(csv_file, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for showroom in detailed_showrooms:
                writer.writerow(showroom)
    except IOError:
        print("I/O error")
    return json.dumps(detailed_showrooms, indent=2)


search_query = "kitchen showrooms near Hotel Indigo in Miami Brickell"
print(get_nearyby_place_info(search_query, max_results=20))
