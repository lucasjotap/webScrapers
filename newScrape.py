from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

name_list = bs.find_all('span', {'class':'green'})
array = [[bs.find_all(text='the prince')], [bs.find_all(text='anna')]]
for name in name_list:
    print(name.get_text())

for item in array:
    for name_occurrences in item:
        print((len(name_occurrences)))

check = "True" if 'anna'.lower() in name_list else 'False'
print(check)
    
