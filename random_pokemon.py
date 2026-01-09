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

def get_random_pokemon():
    random_poke = random.choice(pokemon_list)['name']
    url = f'https://pokeapi.co/api/v2/pokemon/{random_poke}'
    response = requests.get(url)
    return json.loads(response.text)

# Ask the user to choose a pokemon
valid_choice = False

while not valid_choice:
    print('Player 1 - Enter your pokemon or type "random" for a random one:')
    choice = input().lower()

    if choice =="random":
        pokemon_data = get_random_pokemon()
        valid_choice = True
    elif choice in pokemon_names: 
        url = f'https://pokeapi.co/api/v2/pokemon/{choice}'
        response = requests.get(url)
        
        if response.status_code == 200:
            pokemon_data = json.loads(response.text)
            valid_choice = True
        else:
            print("API Error - try again.\n")
    else:
        print("Please choose a valid pokemon.\n")
    
valid_choice2 = False
player2 = 1

while not valid_choice2:
    print('Player 2 - Enter your pokemon or type "random" for a random one or leave blank to battle CPU:')
    choice2 = input().lower()

    if choice2 =="random":
        pokemon_data2 = get_random_pokemon()
        valid_choice2 = True
    elif choice2 in pokemon_names: 
        url = f'https://pokeapi.co/api/v2/pokemon/{choice2}'
        response = requests.get(url)
        
        if response.status_code == 200:
            pokemon_data2 = json.loads(response.text)
            valid_choice2 = True
        else:
            print("API Error - try again.\n")
    else:
        pokemon_data2 = get_random_pokemon()
        valid_choice2 = True
        player2 = 0
        print("No Player 2 present. CPU Pokemon chosen at Random.\n")
    

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))