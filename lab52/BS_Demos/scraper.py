from bs4 import BeautifulSoup as bs

def read_html():
	with open('./page.html','r') as f:
		html = f.read()
		return html


html = read_html()

# create BeautifulSoup object, which represents the document as a nested data structure:
soup = bs(html, 'html.parser')

# --------------------------------- Example 1 -------------------------------- #
# get HTML element:
# #  find(name, attrs, recursive, string, **kwargs)
# elements = soup.find_all('h1', {'id':"h1"})

# # get all attributes
# element = elements[0]
# print(element.attrs)

# # get text content
# print(element.string)

# --------------------------------- Example 2 -------------------------------- #
# # get container and then its children
# data_div = soup.find('div', class_='data')
# # print(data_div)

# # get all divs inside the container:
# divs = data_div.find_all('div')
# # print(divs)
# for div in divs:
# 	print(div.string)

# --------------------------------- Example 3 -------------------------------- #
data = []

data_div = soup.find('div', class_='data')
links = data_div.find_all('a')
for link in links:
	# print(link)
	d = {}
	# d['url'] = link.attrs['href']
	d['url'] = link.href
	d['text'] = link.string
	data.append(d)

print(data)




