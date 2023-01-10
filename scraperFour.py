from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.jodo.org/')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table').children:
    regex = re.compile(r'Understading')
    match_object = regex.search('Understading')
    print(match_object.group())