import requests

from generate_token import Generate_token

def get_shows_episodes(id):
    token_returned = Generate_token.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/shows/{id}/episodes', headers=header)
    return response.json()
