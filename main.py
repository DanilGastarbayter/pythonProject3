import urllib.request
opener = urllib.request.build_opener()
response = opener.open('https://uk.wikipedia.org/')
print(respone.read())
import requests
response = requests.get('https://uk.wikipedia.org/')
print(type(response.content))