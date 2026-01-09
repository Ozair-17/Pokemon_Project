import requests
import json
import random


# Get the list of Pokémon

url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)
pokemon_list = json.loads(response.text)["results"]

for pokemon in pokemon_list:
    print(pokemon["name"])


# Player chooses Pokémon

print("\nEnter your pokemon:")
choice = input().lower()

url = f"https://pokeapi.co/api/v2/pokemon/{choice}/"
response = requests.get(url)

while response.status_code != 200:
    print("Pokemon not found. Try again:")
    choice = input().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{choice}/"
    response = requests.get(url)

player_data = json.loads(response.text)



# CPU gets random Pokémon


random_pokemon = random.choice(pokemon_list)["name"]
url = f"https://pokeapi.co/api/v2/pokemon/{random_pokemon}/"
response = requests.get(url)
cpu_data = json.loads(response.text)



#  height & weight

player_height = int(player_data["height"]) / 10
player_weight = int(player_data["weight"]) / 10

cpu_height = int(cpu_data["height"]) / 10
cpu_weight = int(cpu_data["weight"]) / 10




# Print Pokémon details

print("\nYour Pokémon:")
print(f"Name: {player_data['name']}")
print(f"Height: {player_height} m")
print(f"Weight: {player_weight} kg")


print("\nCPU Pokémon:")
print(f"Name: {cpu_data['name']}")
print(f"Height: {cpu_height} m")
print(f"Weight: {cpu_weight} kg")

print("FIGHT! (MAY THE TALLEST POKEMON WIN)")

if player_height > cpu_height:
        print(f" You win! {player_data['name']} is taller.")
elif cpu_height > player_height:
    print(f" CPU wins! {cpu_data['name']} is taller.")
else:
    print("It's a tie! Both Pokémon are the same height.")
