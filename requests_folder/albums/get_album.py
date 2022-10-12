import requests

from environment import token

def get_album(id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}', headers=header)
    return response