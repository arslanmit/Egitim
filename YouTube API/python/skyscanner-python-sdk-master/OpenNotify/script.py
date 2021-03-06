
import requests
import json

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")


status_code=response.status_code
print(status_code)

status_code=requests.get("http://api.open-notify.org/iss-pass").status_code
print(status_code)

parameters = {"lat": 44.71, "lon": -74}
print(parameters)
print(response)

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.url)
# Print the content of the response (the data the server returned)
print(response.json())

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print(response.content)


# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(best_food_chains)
print(type(best_food_chains))


# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(best_food_chains_string)
print(type(best_food_chains_string))


# Convert best_food_chains_string back into a list
print(json.loads(best_food_chains_string))
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}
print(fast_food_franchise)
print(type(fast_food_franchise))

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(fast_food_franchise_string)
print(type(fast_food_franchise_string))

fast_food_franchise_2=json.loads(fast_food_franchise_string)
print(fast_food_franchise_2)
print(type(fast_food_franchise_2))

parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response)
# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()

print(data)
print(type(data))

print(data["response"][0]["duration"])
print(response.headers)



response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())

in_space_count=response.json()["number"]
