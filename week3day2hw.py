# Exercise 1:
# Create a Method prints an image of your pokemon
# HINT: You may need another attribute as well to store your image url within.

import requests
from IPython.display import Image

class Pokemon():
    def __init__(self, name):
        self.name = name.lower()
        self.types = []
        self.weight = None
        self.abilities = []
        self.imgae_url = None
        self.poke_api_call()
        
        
    def poke_api_call(self):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}/')
    
        data = response.json()
    
        self.name = data['name']
        self.types = [p_type['type']['name'] for p_type in data['types']]
        self.weight = data['weight']
        self.abilities = [p_abilities['ability']['name'] for p_abilities in data['abilities']]
        self.image_url = data['sprites']['other']['official_artwork']['front_default']
        
    def display_sprites(self):
        display(Image(self.image_url, width = "400"))

pikachu = Pokemon('pikachu')
pikachu.display_sprite()
print(pikachu.image_url)


# Exercise 2:
# Create a Method that evolves your Pokemon
# If your pokemon can't evolve any further print a message that says "<name of pokemon> can't evolve."

# Now let's evolve a few

class Pokemon():
    def __init__(self, name):
        self.name = name.lower()
        self.types = []
        self.weight = None
        self.abilities = []
        self.imgae_url = None
        self.species_url = None
        self.poke_api_call()
        
        
    def poke_api_call(self):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}/')
    
        data = response.json()
    
        self.name = data['name']
        self.types = [p_type['type']['name'] for p_type in data['types']]
        self.weight = data['weight']
        self.abilities = [p_abilities['ability']['name'] for p_abilities in data['abilities']]
        self.image_url = data['sprites']['other']['official_artwork']['front_default']
        self.species_url = data['species']['url']
        
    def display_sprites(self):
        display(Image(self.image_url, width = "400"))
        
    def evolve(self):
        res_species = requests.get(self.species_url)
        
        data_species = res_species.json()
        
        evolution_chain = data_species['evolution_chain']['url']
        
        res_evolution = requests.get(evolution_chain)
        
        data_evolution = res_evolution.json()
        
        current_evolution = data_evolution['chain']
        
        while True:
            if current_evolution['species']['name'] == self.name:
                self.name = current_evolution['evoles_to'][0]['species']['name']
                self.poke_api_call()
                break
            elif len(current_evolution['evlves_to']) == 0:
                print(f"{self.name} can't evolve")
                break
            else:
                current_evolution = current_evolution['evolves_to'][0]

pichu = Pokemon('pichu')
pichu.evolve()
pichu.species_url

# Final Exercise:

# Create a Move_Tutor Class that will allow the Pokemon Class to inherit a move list.

# for an added bonus you can make sure that if a pokemon has 4 moves the user can choose one of them to replace with a new move.

import requests

class Move_Tutor:
    def __init__(self):
        self.move_list = []
        self.current_moves = ['mega-punch', 'pay-day', 'thunder-punch', 'slam']    
        
    def show_moves(self):
        print(f"{self.name}'s moves'")
        
        for move in current_moves:
            print(move)
    
    def display_move_list(self):
        print(f"{self.name}'s teachable moves: ")
        
        for move in display_move_list:
            print(move, end=" ")
            
        print()
    
    def teach_move(self):
        self.display_move_list()
        print()
        self.show_moves()
        
        new_move = input("What move would you like to learn? ")
        
        if new_move.lower() not in self.move_list:
            print(f"{new_move} is not valid")
            return
        
        if len(self.current_moves) >= 4:
            replace_move = input("You already have 4 moves, which one would like to replace?")
            
            for idx, move in enumerate(self.current_moves):
                if replace_move.lower() == move:
                    self.current_moves[idx] = new_move.lower()
                    print(f'{move} replaced with {new_move}')
                    break
        else:
            self.current_moves.append(new_move.lower())
            print(f"Added {new_move} to {self.name}'s moves")

class Pokemon(Move_Tutor):
    def __init__(self, name):
        self.name = name.lower()
        self.types = []
        self.weight = None
        self.abilities = []
        self.imgae_url = None
        self.species_url = None
        super().__init__()
        self.poke_api_call()
        
        
    def poke_api_call(self):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}/')
    
        data = response.json()
    
        self.name = data['name']
        self.types = [p_type['type']['name'] for p_type in data['types']]
        self.weight = data['weight']
        self.abilities = [p_abilities['ability']['name'] for p_abilities in data['abilities']]
        self.image_url = data['sprites']['other']['official_artwork']['front_default']
        self.species_url = data['species']['url']
        
        moves = data['moves']
        
        for move in moves:
            self.move_list.append(move['move']['name'])

pikachu = Pokemon('pickachu')
pikachu.move_list
pikachu.teach_move()
pikachu.show_moves()