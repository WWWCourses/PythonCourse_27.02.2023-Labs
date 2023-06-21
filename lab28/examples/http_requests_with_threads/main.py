from fileinput import filename
import requests
import re
from bs4 import BeautifulSoup
import time

import threading

def get_links(base_url):
	html = get_page_content(base_url)
	soup = BeautifulSoup(html, 'html.parser')  # type: ignore

	pubs_divs = soup.select('#module_1_1 .row-fluid > .span8')
	pubs_urls = []

	for pub_div in pubs_divs:
		a = pub_div.find('a')
		pubs_urls.append(a['href'])


	return pubs_urls


def get_page_content(url):
	print(f'making request to {url}')
	r = requests.get(url)

	if r.ok:
		return r.text

def save_to_file(content, filename):
	try:
		with open(filename, 'w',encoding='utf-8') as f:
			f.write(content)
	except Exception as e:
		print(f'Can not write to file: {filename}: {str(e)}')
		exit(-1)

def process_page(url):
	print(f'Processing page: {url} from {threading.current_thread().name}')
	html = get_page_content(url)

	filename_re = re.compile(r'(\d+)')
	filename_match = filename_re.search(url)
	if filename_match:
		filename = filename_match[1]  + '.html'
	else:
		filename = 'no_name'

	save_to_file(html, filename)

def main():
	server_root ='https://bnr.bg'
	base_url = server_root + '/hristobotev/radioteatre/list'
	seed = get_links(base_url)


	for href in seed:
		url = server_root + href
		process_page(url)

def main_threaded():
	server_root ='https://bnr.bg'
	base_url = server_root + '/hristobotev/radioteatre/list'
	seed = get_links(base_url)


	for href in seed:
		url = server_root + href
		tr = threading.Thread(target=process_page, args=(url,))
		tr.start()
		tr.join()


if __name__=="__main__":
	start = time.time()
	main()
	end = time.time()
	print(f'sequential time taken: {end-start}')

	start = time.time()
	main_threaded()
	end = time.time()
	print(f'threaded time taken: {end-start}')