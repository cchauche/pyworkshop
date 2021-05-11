import requests

API_URL = "http://shibe.online/api/shibes"

params = {
    "count": 10
}

api_response = requests.get(API_URL, params=params)

print(f"Shibe API Response status code is: {api_response.status_code}")

json_data = api_response.json()

print("Here is a list of URLs for dog pictures:")
for url in json_data:
    print(f"\t {url}\n")
