import requests
import threading

def download_image(url):
	file_name = url.split('/')[4]+".jpg"

	# get image bytes
	print(f"Start downloading {url}")
	response = requests.get(url)

	# write image to file
	with open(file_name, 'wb') as fh:
		fh.write(response.content)

	print(f"File saved to {file_name}")

if __name__ == "__main__":
	images  = [
		"https://unsplash.com/photos/CTflmHHVrBM/download?force=true",
		"https://unsplash.com/photos/pWV8HjvHzk8/download?force=true",
		"https://unsplash.com/photos/1jn_3WBp60I/download?force=true",
		"https://unsplash.com/photos/8E5HawfqCMM/download?force=true",
		"https://unsplash.com/photos/yTOkMc2q01o/download?force=true"
	]

	tread_pool = []
	for img in images:
	# 	download_image(img)
		tr = threading.Thread(target=download_image, args=(img,))
		tread_pool.append(tr)
		tr.start()

