import requests
from bs4 import BeautifulSoup
import re
import datetime
from dateutil.relativedelta import relativedelta


URL = 'https://www.jobs.bg/en/front_job_search.php?subm=1&keywords%5B%5D=python'

class Crawler:
	def __init__(self, url) -> None:
		self.url = url

	def get_html(self,url):
		try:
			r = requests.get(url)
		except requests.RequestException:
			r = requests.get(url,verify=False)
		except Exception as e:
			print(f'Can not get url: {url}: {str(e)}!')
			exit(-1)

		# set content encoding explicitely
		r.encoding="utf-8"

		if r.ok:
			return r.text
		else:
			print('The server did not return success response. Bye...')
			exit

	def run(self):
		html = self.get_html(self.url)
		# print(html)
		self.scraper = Scraper(html)
		self.scraper.get_jobs()



class Scraper:
	def __init__(self, html):
		self.html = html
		self.soup = BeautifulSoup(html, 'html.parser')

	def get_jobs(self):
		data = {}
		job_selector = '#listContainerScrollable div.mdc-card div.mdc-layout-grid__inner'
		div_jobs = self.soup.select(job_selector)
		for job in div_jobs:
			# print('*'*40)
			# print(job)
			# print('*'*40)
			# date = job.select_one('div.card-date').get_text()
			date = next(job.select_one('div.card-date').chiuldren)
			print(f'date)


if __name__=="__main__":
	crawler = Crawler(URL)
	crawler.run()