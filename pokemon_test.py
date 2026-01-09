import requests
import json

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)
player_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
""" print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name'])) """

""" print(pokemon_data['moves'][0]['move']['name'])
print(type(pokemon_data))
 """

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
