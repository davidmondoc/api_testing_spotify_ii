import requests

from generate_token import Generate_token

def get_several_artists(list_of_ids):
    token_returned = Generate_token.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/artists?ids={list_of_ids}', headers=header)
    return response.json()
