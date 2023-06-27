from soupMaster import URL_reader
from bs4 import BeautifulSoup
import pandas as pd

reader = URL_reader('https://www.imdb.com/chart/top/')

table, rows = reader.process_url()
movies = []
for row in rows:
	title_column = row.find('td', class_='titleColumn')
	if title_column:
		title_link = title_column.find("a")
		if title_link:
			title = title_link.text.strip()
			year = title_column.find('span', class_="secondaryInfo").text.strip("()")
			movie_dictionary = {"name":title, "year":year}
			movies.append(movie_dictionary)

df = pd.DataFrame(movies)
print(df)