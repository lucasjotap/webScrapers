from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'lxml')

data = bs.find_all(lambda tag: len(tag.attrs) == 1)
print(type(data))

for datum in data:
    print(datum)
    break
print(data[0])