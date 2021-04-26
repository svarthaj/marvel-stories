import os, requests, random

from .auth import get_auth_params
from .characters import parse_characters

# Process env variables
base_url = os.environ['BASE_URL'] 

def get_random_story(hero_id, total_stories):
    # Select a random story by setting the offset to a number in [0,total_stories) and the limit to 1
    offset = random.randint(0,total_stories-1)
    params = {'characters': hero_id, 'offset': offset, 'limit': 1}
    params.update(get_auth_params())
    story = requests.get(base_url+'/v1/public/stories', params=params) 
    return story.json()

def parse_story(hero_name, story):
    story_info = {}
    result = story['data']['results'][0]

    story_info['hero_name'] = hero_name
    story_info['title'] = result['title']
    story_info['description'] = result['description'] if len(result['description']) > 0 else 'No description available.'
    story_info['characters'] = parse_characters(result['characters'])
    story_info['attribution_text'] = story['attributionText']
    
    return story_info

def get_story_info(hero_name):
    # Get the total count of stories with selected hero
    params = {'name': hero_name}
    params.update(get_auth_params())
    character = requests.get(base_url+'/v1/public/characters', params=params).json()['data']['results'][0]
    hero_id = character['id']
    total_stories = character['stories']['available']

    rand_story = get_random_story(hero_id, total_stories)

    story_info = parse_story(hero_name, rand_story)

    return story_info
    