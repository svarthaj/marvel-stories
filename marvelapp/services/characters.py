import os, requests, random

from .auth import get_auth_params

# Process env variables
base_url = os.environ['BASE_URL'] 

def parse_characters(characters_list):
    characters = {}
    for item in characters_list['items']:
        characters[item['name']] = get_character_info(item['resourceURI'])
    
    return characters

def get_character_info(character_uri):
    params = get_auth_params()
    character = requests.get(character_uri, params=params).json()['data']['results'][0]
    
    return {    'name': character['name'], 
                'img': '.'.join((character['thumbnail']['path'],character['thumbnail']['extension'])) }
