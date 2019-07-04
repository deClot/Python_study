import requests

def calc_age(uid):
    token = '7c40e5767c40e5767c40e576f17c2b955277c407c40e576215a1da5cf3ef910dd4f6bd0'
    url  = 'https://api.vk.com/method/{}.get?v=5.71&access_token={}&user_ids={}'
    
    response = requests.get(url.format('users',token,uid)).json()
    user_id = response['response'][0]['id']
    print(user_id)

    url  = 'https://api.vk.com/method/{}.get?v=5.71&access_token={}&user_id={}&fields=bdate'
    response = requests.get(url.format('friends', token, user_id)).json()
    #number_friends = response['response']['count']
    friends = response['response']['items']

    #print(number_friends)
    data_hist = {}
    for friend in friends:
        #print(friend)
        try:
            age = 2019 - int(friend['bdate'].split('.')[2])
            data_hist[age] = data_hist.get(age,0) + 1
        except:
            continue

    data_hist = data_hist.items()
    s = sorted(data_hist, key=lambda x: x[0])
    return sorted(s, key=lambda x: x[1], reverse=True)
        

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)


