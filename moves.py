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
#player
print("\nYour Pokémon:")
print(f"Name: {player_data['name']}")
#cpu
print("\nCPU Pokémon:")
print(f"Name: {cpu_data['name']}")


#### Getting random moves 

player_moves = []

for move in player_data["moves"]:
    name_of_move = move["move"]["name"]
    player_moves.append(name_of_move)

cpu_moves = []

for move in cpu_data["moves"]:
    name_of_move = move["move"]["name"]
    cpu_moves.append(name_of_move)


            #selecting 4 random 

if len(player_moves) >= 5:
    player_move_count = 5

else:
    player_move_count =len(player_moves)

if len(cpu_moves) >= 5:
    cpu_move_count = 5
else:
    cpu_move_count = len(cpu_moves)

#note random.sample takes in (list,number) as arguments
player_4_moves = random.sample(player_moves,player_move_count)
cpu_4_moves = random.sample(cpu_moves,cpu_move_count)

print("Your 5 moves:")
for move in player_4_moves:
    print("-", move)

print("CPU has selected its moves- you cannot see this")
print("Choose your move...")

## player selects their move 
player_move_selection = input().lower()
#cpu selects their move

cpu_move_selection = random.choice(cpu_4_moves)
print(f"You chose: {player_move_selection} (length {len(player_move_selection)})")
print(f"CPU chose: {cpu_move_selection} (length {len(cpu_move_selection)})")


# battle to see whos string length is longer 

if len(player_move_selection) > len(cpu_move_selection):
    print(f" You win! '{player_move_selection}' is longer than '{cpu_move_selection}'.")
elif len(cpu_move_selection) > len(player_move_selection):
    print(f"CPU wins! '{cpu_move_selection}' is longer than '{player_move_selection}'.")
else:
    print(f"It's a tie.Both moves have length {len(player_move_selection)}.")