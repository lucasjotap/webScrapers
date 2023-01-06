from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), "html.parser")

storage_list = bs.find_all('span', {'class':{'green', 'red'}})
word_array = bs.find_all(text='Anna Pavlovna')

regex = re.compile('Anna')
for item in word_array:
    match_object = regex.search(item)
    print(f"The name is {match_object.group().lower()}")
    break