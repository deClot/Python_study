import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()

email = users[0]['email']

new_user = {'email': 'john@doe.com',
            'first_name': 'John'
            }

response = requests.post('https://jsonplaceholder.typicode.com/users', new_user)
print(response.content)