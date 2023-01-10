from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.jodo.org/')
bs = BeautifulSoup(html, 'html.parser')

for sibling in bs.find('table').tr.next_siblings:
    print(sibling)