import requests

from generate_token import Generate_token

def get_user_saved_shows():
    token_returned = Generate_token.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/me/shows', headers=header)
    return response.json()
