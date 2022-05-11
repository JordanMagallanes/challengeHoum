
'''
    Author: Jordan Javier Magallanes Flores
    Python: 3.6.9
'''

import requests # Librery to request the API
# Instalations: $ pip install requests
import json # Librery to have 

def firstChallenge(): #Get how many pokemons have "at" in their names and have 2 "a" in their name, including the first "at".
    if __name__ == '__main__':
        url = 'https://pokeapi.co/api/v2/pokemon/'
        id = {'offset': '0','limit': '10000'}
        response = requests.get(url, params=id)

        pokemons = []
        validname = []
        rule1 = 0 # two leters "a" in the name
        rule2 = 0 # have "at" in the name

        if response.status_code == 200:
            response_json = response.json()
            results = response_json['results']
            
            for result in results:
                name = result['name']

                pokemons.append(name)

            # Verify the rules
            for pokemon in pokemons:
                for i in range(len(pokemon)):
                    if pokemon[i] == 'a':
                        if (i+1) < len(pokemon) and pokemon[i+1] == 't':
                            rule2+=1
                        rule1+=1
                if rule1 == 2 and rule2 > 1:
                    validname.append(pokemon)

                rule1 = 0
                rule2 = 0

        print(len(validname))


def secondChallenge(): # How many species of Pokémon can Raichu breed with?

    if __name__ == '__main__':
        url = 'https://pokeapi.co/api/v2/egg-group/'
        id = {'offset': '0','limit': '1000'}
        response = requests.get(url, params=id)

        urlspecies = []
        raichuspecie = []
        procreate = []
        procreateunique = []

        if response.status_code == 200:
            response_json = response.json()
            results = response_json['results']

            for result in results:
                name = result['url']

                urlspecies.append(name)

            for i in urlspecies:
                response2 = requests.get(i)

                if response2.status_code == 200:
                    response_json = response2.json()
                    species = response_json['pokemon_species']

                    for specie in species:
                        nspecie = specie['name']

                        if nspecie == 'raichu':
                            raichuspecie.append(i)
            
            for i in raichuspecie:
                response3 = requests.get(i)

                if response3.status_code == 200:
                    response_json = response3.json()
                    species = response_json['pokemon_species']

                    for specie in species:
                        nspecie = specie['name']

                        if 'nspecie' in procreate:
                            continue
                        else:
                            procreate.append(nspecie)
        # Remove duplicate pokemons
            for pokemon in procreate:
                if not pokemon in procreateunique:
                    procreateunique.append(pokemon)
            print(len(procreateunique))

def thirdChallenge(): # Maximum and minimum weight of first generation fighting type pokémon (whose id is less than or equal to 151)
    if __name__ == '__main__':
        url = 'https://pokeapi.co/api/v2/type/'
        
        weightsMinMax = []
        weights = []

        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()
            results = response_json['results']
            
            # Get all pokemons of fighting type
            for types in results:
                if types['name'] == 'fighting':
                    urltype = types['url']
                    
            # Get all pokemoms of first generation

            response2 = requests.get(urltype)

            if response2.status_code == 200:
                response_json = response2.json()
                generations = response_json['game_indices']
                
                for generation in generations:
                    ngeneration = generation['generation']

                    if ngeneration['name'] == 'generation-i':
                        urlgeneration = ngeneration['url']

                response3 = requests.get(urltype)

                if response3.status_code == 200:
                    response_json = response3.json()    

                    pokemons = response_json['pokemon']

                    for pokemon in pokemons:
                        npokemon = pokemon['pokemon']

                        urlpokemon = npokemon['url']
                    
                    # Get characteristics of pokemon (with id less or equal to 151)

                        response4 = requests.get(urlpokemon)

                        if response4.status_code == 200:
                            response_json = response4.json() 
                            ids = response_json['id']
                            if ids <= 151:
                                weight = response_json['weight']
                                weights.append(weight)
                    weights.sort()
                    
                    weightsMinMax.append(weights.pop(0))
                    weightsMinMax.append(weights.pop())

                    print(weightsMinMax)


firstChallenge()
secondChallenge()
thirdChallenge()

