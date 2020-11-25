import requests
import json

#headers = 'Accept: application/json' 


def chuckJoke(): 
    request_site = r"https://api.chucknorris.io/jokes/random"

    data = requests.get(request_site)
    tt = json.loads(data.text)


    print(tt["value"])

def dadJoke():
    request_site = r"https://icanhazdadjoke.com/"

    data = requests.get(request_site)
    tt = data.text

    print(tt)

chuckJoke()
#dadJoke() doesnt work at the moment
