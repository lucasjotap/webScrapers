import tweepy
import requests
import random
import json

consumer_key = 'l6UYJ1GpDNXrzbjrNa2P7VuLl'
consumer_secret = 'z1u5QgoWxlCJoUVoC7YFBKgEtB6q5pygfHtdVxMC1bjFjlytD6'
access_token = '1584539030452113408-sHtahTiShpwtu5vrG6Iu0bmx2OGncM'
access_token_secret = 'PWHkJrF0orhXJuFPsCsknbTTvgWThnuAqktVSeEPnsOQB'

def main():
    country = 'Brazil'
    api_url = 'https://api.api-ninjas.com/v1/inflation?country={}'.format(country)
    response = requests.get(api_url, headers={'X-Api-Key': 'yk1iymINibQQoWZaeqzFgA==9GnNP6zxuBDwK98m'})
    if response.status_code == requests.codes.ok:
        print("Passed!")
    else:
        print("Error:", response.status_code, response.text)

    global string 
    data_str = response.text
    data_list = json.loads(data_str)
    word = [value for index in data_list for value in index.values()]
    string = f"Country of {word[0]}, {word[1]} -- during the period of {word[2]} has a monthly rate of {word[3]} and an yearly rate of {word[4]}"

def auth(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(random.randint(1, 2000000))
    api.update_status(string)

main()
auth(consumer_key, consumer_secret, access_token, access_token_secret)
