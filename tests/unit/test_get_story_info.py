from marvelapp.services.stories import get_story_info

def test_get_story_info(client):
    '''
    GIVEN a Hero name
    WHEN the function is called
    THEN check that it return a valid story
    '''
    story = get_story_info('Spider-Man')
    print(story)
    assert all(key in story for key in ['hero_name', 'title', 'description', 'characters', 'attribution_text'])