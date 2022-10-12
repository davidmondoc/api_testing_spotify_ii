from requests_folder.albums.get_album import get_album

response = get_album('1mc8M9eR9ZIBxqWA2CA4Wo')
print(response.json())