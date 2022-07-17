import httpx, time, json

# CHANGE THESE
BEARER_TOKEN = ''
USERNAME = ''

with httpx.Client() as client:
    USERID = ''
    req = client.get(f'https://api.twitter.com/2/users/by?usernames={USERNAME}', headers={'Authorization': f'Bearer {BEARER_TOKEN}'})

    if req.status_code == 200:
        print(f'Got {USERNAME}\'s ID: {req.json()["data"][0]["id"]}')
        USERID = req.json()['data'][0]['id']
    elif req.status_code == 404:
        print(f'{USERNAME} not found')
        exit(1)
    elif req.status_code == 429:
        print('Rate limit exceeded')
        exit(1)
    elif req.status_code == 401:
        print('Unauthorized, Bearer Token is invalid')
    else:
        print(f'Unknown error: {req.status_code}')
        exit(1)

    req = client.get(f'https://api.twitter.com/2/users/{USERID}/tweets?exclude=replies,retweets',  headers={'Authorization': f'Bearer {BEARER_TOKEN}'})
    res = req.json()
    print('Got ' + str(res['meta']['result_count']))
    nextToken = res['meta']['next_token']
    with(open('tweets.json', 'r+')) as f:
        try:
            oldData = json.load(f)
        except:
            oldData = []

        for tweet in res['data']:
            if('https://t.co' in tweet['text']):
                continue
            oldData.append(tweet['text'])
        f.seek(0)
        f.truncate()
        f.write(json.dumps(oldData, indent=4))
        print('Saved to tweets.json')

        while nextToken != None:
            req = client.get(f'https://api.twitter.com/2/users/{USERID}/tweets?exclude=replies,retweets&pagination_token={nextToken}',  headers={'Authorization': f'Bearer {BEARER_TOKEN}'})
            res = req.json()
            try:
                nextToken = res['meta']['next_token']
            except:
                break
            for tweet in res['data']:
                if('https://t.co' in tweet['text']):
                    continue
                oldData.append(tweet['text'])
            f.seek(0)
            f.truncate()
            f.write(json.dumps(oldData, indent=4))
            print('Saved to tweets.json')
            time.sleep(2)


    time.sleep(1)