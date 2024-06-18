import requests

# Function to get the moves of a Pokémon in a specific version group
def get_pokemon_moves(pokemon_name, version_group_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        moves = []
        for move in data['moves']:
            for version_group in move['version_group_details']:
                if version_group['version_group']['name'] == version_group_name:
                    moves.append(move['move']['name'])
        return moves
    else:
        print(f"Failed to get data for {pokemon_name}")
        return None

# Get Jigglypuff's moves in the Ruby-Sapphire version group
jigglypuff_moves = get_pokemon_moves('jigglypuff', 'ruby-sapphire')

# Get Haunter's moves in the Ruby-Sapphire version group
haunter_moves = get_pokemon_moves('haunter', 'ruby-sapphire')

# Ensure we got valid move lists
if jigglypuff_moves is not None and haunter_moves is not None:
    # Find moves that Jigglypuff has but Haunter does not have
    unique_moves = [move for move in jigglypuff_moves if move not in haunter_moves]

    # Print the number of unique moves
    print(f"Jigglypuff has {len(unique_moves)} moves that Haunter does not have in the Ruby-Sapphire version.")
else:
    print("Failed to retrieve move data for one or both Pokémon.")
