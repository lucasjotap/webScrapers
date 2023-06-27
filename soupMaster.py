import requests
from bs4 import BeautifulSoup

class URL_reader:
	"""
	Defining the reader for scraping.
	"""
	def __init__(self, url):
		self.url = url

	def read_url(self):
		url_res = requests.get(self.url)
		return url_res
		
	def process_url(self):
		processed_url = BeautifulSoup(self.read_url().content, 'html.parser')
		table = processed_url.find("table", class_='chart')
		row = table.find_all("tr")
		return table, row
