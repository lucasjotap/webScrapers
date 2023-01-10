from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.jodo.org/')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table').children:
    try:
        regex = re.compile(child)
        match_object = regex.search('Understanding')
        print(match_object.group())
    except AttributeError or TypeError as e:
        print(e)
    