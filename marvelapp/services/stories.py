import os, requests, random

from .auth import get_auth_params
from .characters import parse_characters

# Process env variables
base_url = os.environ['BASE_URL'] 
hero_id = os.environ['FAVORITE_HERO_ID']
hero_name = os.environ['FAVORITE_HERO_NAME']

def get_random_story(total_stories):
    # Select a random story by setting the offset to a number in [0,total_stories) and the limit to 1
    offset = random.randint(0,total_stories-1)
    params = {'characters': hero_id, 'offset': offset, 'limit': 1}
    params.update(get_auth_params())
    story = requests.get(base_url+'/v1/public/stories', params=params) 
    return story.json()

def parse_story(story):
    story_info = {}
    result = story['data']['results'][0]

    story_info['hero_name'] = hero_name
    story_info['title'] = result['title']
    story_info['description'] = result['description'] if len(result['description']) > 0 else 'No description available.'
    story_info['characters'] = parse_characters(result['characters'])
    story_info['attribution_text'] = story['attributionText']
    
    return story_info

def get_story_info():
    # Get the total count of stories with selected hero
    params = {'characters': hero_id}
    params.update(get_auth_params())
    stories = requests.get(base_url+'/v1/public/stories', params=params)
    total_stories = stories.json()['data']['total']

    rand_story = get_random_story(total_stories)

    story_info = parse_story(rand_story)

    return story_info
    