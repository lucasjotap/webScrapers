from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def get_links(pageUrl):
    global pages
    html = urlopen(f'http://en.wikipedia.org{pageUrl}')
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                get_links(new_page)

get_links('')
