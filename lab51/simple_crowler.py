import requests
from bs4 import BeautifulSoup as bs

class Crawler():
	def __init__(self,url) -> None:
		self.url = url

	def get_html(self):
		r = requests.get(self.url)
		if r.ok:
			self.html = r.text
		else:
			return 'no content'

	def get_data(self):
		soup = bs(self.html, 'html.parser')
		# divs = soup.find('div')
		# print(divs)
		items = soup.select('div.item h3')
		for item in items:
			print(item.text)




url = 'http://127.0.0.1:8080/'
crawler = Crawler(url)

crawler.get_html()
crawler.get_data()


