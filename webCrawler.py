import requests 

# Wikipedia
URL = "https://www.wikipedia.org/"
resp = requests.get(URL)
print(resp.status_code)
print(resp.text)