from marvelapp import create_app
import os

def test_index(client):
    '''
    GIVEN a Flask app
    WHEN the index ('/') is requested
    THEN check that the response is valid
    '''
    response = client.get('/')
    assert response.status_code == 200
    assert os.environ.get('FAVORITE_HERO_NAME').encode() in response.data