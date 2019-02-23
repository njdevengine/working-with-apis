# Dependencies
import requests
url = "http://api.worldbank.org/v2/"

# Get the list of lending types the world bank has
lending_response = requests.get(f"{url}lendingTypes?format=json").json()
lending_types = [lending_type["id"] for lending_type in lending_response[1]]

# Next, determine how many countries fall into each lending type.
# Hint: Look at the first element of the response array.
country_count_by_type = {}
for lending_type in lending_types:
    query = f"{url}countries?lendingType={lending_type}&format=json"
    response = requests.get(query).json()
    country_count_by_type[lending_type] = response[0]["total"]
    
# Print the number of countries of each lending type
for key, value in country_count_by_type.items():
    print(f"The number of countries with lending type {key} is {value}.")
