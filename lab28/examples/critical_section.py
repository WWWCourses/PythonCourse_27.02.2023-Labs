import threading
from time import time, sleep


def worker():

	global counter

	sleep(1)
	for _ in range(10):
		lock.acquire()
		counter += 1
		lock.release()

def main_seq():
	worker()
	worker()
	worker()

	print(f'counter={counter}')

def main_conc():
	threads = []
	threads_count = 3

	# make threads list
	for _ in range(threads_count):
		tr = threading.Thread(target=worker)
		threads.append(tr)

		tr.start()

	for tr in threads:
		tr.join()

	print(f'counter={counter}')


start = time()
counter = 0
lock = threading.Lock()
# main_seq()
main_conc()
end = time()
print(f'Time: {end-start}')


