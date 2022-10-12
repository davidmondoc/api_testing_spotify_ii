import requests

from generate_token import Generate_token

def get_severak_shows(list_of_ids):
    token_returned = Generate_token.authorization()
    header = {'Authorization': token_returned}
    response = requests.put(f'https://api.spotify.com/v1/shows?ids={list_of_ids}', headers=header)
    return response.json()
