#!/usr/bin/env python3

import requests
import pprint

def main():
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/1").json()
    print(f"Name of my pokimon: {pokeapi['name']}")
    #pprint.pprint(pokeapi['sprites'])
    print(f"URL: {pokeapi['sprites']['other']['official-artwork']['front_default']}")
    #print("")
    game_indices = pokeapi['game_indices']
    #pprint.pprint(game_indices)
    indice_count = 0
    for indice in game_indices:
        #print(indice)
        indice_count +=1
    print(f"Total Number of game_indices for {pokeapi['name']} is \"{indice_count}\"")
    #print("")
    poki_moves = pokeapi['moves']
<<<<<<< HEAD
    #print(poki_moves)
    #move_count = 0
    for mv in poki_moves:
        print(mv['move']['name'])
=======
    for mv in poki_moves:
        print(mv['move']['name'])

>>>>>>> 2420664b8f20b1dc68cfe55d7f971d526384e952
        

if __name__ == "__main__":
    main()
