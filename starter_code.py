import requests
import json

# Get the list of Pokémon from the API
url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)

pokemon_list = json.loads(response.text)["results"]

# Print Pokémon names
for pokemon in pokemon_list:
    print(pokemon["name"])

# Ask the user to choose a Pokémon
print("\nEnter your pokemon:")
choice = input().lower()

# Get the selected Pokémon's data
url = f"https://pokeapi.co/api/v2/pokemon/{choice}/"
response = requests.get(url)

pokemon_data = json.loads(response.text)

# Get ability
abilities = pokemon_data["abilities"][0]
ability = abilities["ability"]

# Format height and weight
height = int(pokemon_data["height"])
weight = int(pokemon_data["weight"])

height_formatted = height / 10  # meters
weight_formatted = weight / 10  # kilograms

# Print Pokémon details
print("\nPokémon Details")
print(f"Name: {pokemon_data['name']}")
print(f"Weight: {weight_formatted} (kgs)")
print(f"Height: {height_formatted} (m)")
print(f"Ability: {ability['name']}")
