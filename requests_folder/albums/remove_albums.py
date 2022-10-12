import requests

from generate_token import Generate_token

def remove_albums(list_of_ids):
    token_returned = Generate_token.authorization()
    header = {'Authorization': token_returned}
    response = requests.delete(f'https://api.spotify.com/v1/me/albums?ids={list_of_ids}', headers=header)
    return response.json()
