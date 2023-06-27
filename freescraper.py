from bs4 import BeautifulSoup
from urllib.request import urlopen 
import re

html = urlopen('https://www.accuweather.com/pt/br/curitiba/44944/daily-weather-forecast/44944')
bs = BeautifulSoup(html.read(), 'lxml')
print(bs.h1)