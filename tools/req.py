import requests

URL = 'https://botw-compendium.herokuapp.com/api/v3/compendium/entry/white-maned_lynel'
response = requests.get(URL)
print(response.text)
data = response.json()

print(data['data']['description'])
