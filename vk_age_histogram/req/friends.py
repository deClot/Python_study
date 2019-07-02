import requests

def calc_age(uid):
    token = '7c40e5767c40e5767c40e576f17c2b955277c407c40e576215a1da5cf3ef910dd4f6bd0'
    url  = 'https://api.vk.com/method/{}.get?v=5.71&access_token={}&user_ids={}'
    
    response = requests.get(url.format('users',token,uid)).json()
    user_id = response['response'][0]['id']
    print(user_id)

    url  = 'https://api.vk.com/method/{}.get?v=5.71&access_token={}&user_id={}&fields=bdate'
    response = requests.get(url.format('friends', token, user_id))
    print(response.text)
 
#params = {'user_id': us_id, 'fields': 'bdate'}

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
