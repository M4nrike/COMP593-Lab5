'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():

    # Test out the get_pokemon_info() function
    poke_info =  get_pokemon_info("Rockruff")
    print (poke_info)   

    #Add breakpounts to see the dictionary populated                     
    
    return

def get_pokemon_info(pokemon_name):

    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    pokemon_name = str(pokemon_name).lower().strip()

    # TODO: Build a clean URL and use it to send a GET request
    clean_url = f'{POKE_API_URL}{pokemon_name}'

    print (f'Getting information for {pokemon_name}...', end='')
    api_request = requests.get(clean_url)
        
    if api_request.status_code == requests.codes.ok:

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
        print("Success")
        return api_request.json()
        
    # TODO: If the GET request failed, print the error reason and return None
    else:
        print (f"Failure in gathering the information. \n Status code: {api_request.status_code} ({api_request.reason})")
        return None
    

if __name__ == '__main__':
    main()