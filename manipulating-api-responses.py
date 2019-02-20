# Dependencies
import requests
import json

# Performing a GET Request and saving the 
# API's response within a variable
url = "https://api.spacexdata.com/v2/rockets/falcon9"
response = requests.get(url)
response_json = response.json()
print(json.dumps(response_json, indent=4, sort_keys=True))

# It is possible to grab a specific value 
# from within the JSON object
print(response_json["cost_per_launch"])

# It is also possible to perform some
# analyses on values stored within the JSON object
number_payloads = len(response_json["payload_weights"])
print(f"There are {number_payloads} payloads.")

# Finally, it is possible to reference the
# values stored within sub-dictionaries and sub-lists
payload_weight = response_json["payload_weights"][0]["kg"]
print(f"The first payload weighed {payload_weight} Kilograms")
