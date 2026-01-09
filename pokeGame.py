import requests
import json

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Player 1 chooses a pokemon
print('Player 1 - Enter your pokemon:')
choice1 = input().lower()

url = f'https://pokeapi.co/api/v2/pokemon/{choice1}/'
response = requests.get(url)
pokemon1_data = json.loads(response.text)

height1 = pokemon1_data['height'] / 10

print('Player 1 Pokemon:', pokemon1_data['name'])
print('Height:', height1, '(m)')

# Player 2 chooses a pokemon
print('\nPlayer 2 - Enter your pokemon:')
choice2 = input().lower()

url = f'https://pokeapi.co/api/v2/pokemon/{choice2}/'
response = requests.get(url)
pokemon2_data = json.loads(response.text)

height2 = pokemon2_data['height'] / 10

print('Player 2 Pokemon:', pokemon2_data['name'])
print('Height:', height2, '(m)')

# Compare heights
print('\nResult:')
if height1 > height2:
    print('Player 1 wins! Taller Pokemon.')
elif height2 > height1:
    print('Player 2 wins! Taller Pokemon.')
else:
    print('It is a draw! Same height.')
