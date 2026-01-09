import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

pokemon_names = [p['name'] for p in pokemon_list]

def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    return json.loads(response.text)

def get_random_pokemon():
    random_name = random.choice(pokemon_names)
    return get_pokemon_data(random_name)

#
valid_choice = False
while not valid_choice:
    print('\nPlayer 1 - Enter your pokemon or type "random":')
    choice1 = input().lower()

    if choice1 == "random":
        pokemon1 = get_random_pokemon()
        valid_choice = True
    elif choice1 in pokemon_names:
        pokemon1 = get_pokemon_data(choice1)
        valid_choice = True
    else:
        print("Please choose a valid pokemon.")

# Player 2 
valid_choice = False
while not valid_choice:
    print('\nPlayer 2 - Enter your pokemon or type "random":')
    choice2 = input().lower()

    if choice2 == "random":
        pokemon2 = get_random_pokemon()
        valid_choice = True
    elif choice2 in pokemon_names:
        pokemon2 = get_pokemon_data(choice2)
        valid_choice = True
    else:
        print("Please choose a valid pokemon.")

# Heights (converted to metres)
height1 = pokemon1['height'] / 10
height2 = pokemon2['height'] / 10

# Print results
print('\nPlayer 1 Pokemon:', pokemon1['name'])
print('Height:', height1, '(m)')

print('\nPlayer 2 Pokemon:', pokemon2['name'])
print('Height:', height2, '(m)')

# Compare heights
print('\nResult:')
if height1 > height2:
    print('Player 1 wins! Taller pokemon.')
elif height2 > height1:
    print('Player 2 wins! Taller pokemon.')
else:
    print('It is a draw! Same height.')
