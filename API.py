from pip._vendor import requests

with open('ID.txt') as f:
    id = f.read()
access_token = '18dc4bd918dc4bd918dc4bd9a718ae0b0c118dc18dc4bd94613ce6570f08cbe5258ffe8'
v='5.52'

output = requests.get('https://api.vk.com/method/friends.get?user id=' + id + '&v=' + v + '&access_token=' + access_token).json()

for people in output['response']['items']:
    data = requests.get('https://api.vk.com/method/users.get?user id=' + str(people) + '&v=' + v + '&access_token=' + access_token).json()

    name = data['response'][0]['name']
    surname = data['response'][0]['surname']
    print(name + ' ' + surname)