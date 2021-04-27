def test_index(client):
    '''
    GIVEN a Flask app
    WHEN the index ('/') is requested
    THEN check that the response is valid
    '''
    response = client.get('/')
    assert response.status_code == 200

def test_story(client):
    '''
    GIVEN a Flask app
    WHEN the a hero name is posted at ('/story') 
    THEN check that the response is valid
    '''
    response = client.post('/story', data={'hero_name': 'Spider-Man'})
    assert response.status_code == 200
    assert 'Spider-Man'.encode() in response.data