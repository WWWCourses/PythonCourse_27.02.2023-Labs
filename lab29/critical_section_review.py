import threading
from time import time

def worker():
	global counter

	print(f'counter = {counter}')

	lock.acquire()
	for i in range(1_000_000):
		counter += 1
	lock.release()



def sequential():
	for _ in range(5):
		worker()

	print(f'counter in sequential: {counter}')


def threaded():
	# create some treads to count together:
	thread_pool = []

	for i in range(5):
		tr = threading.Thread(target=worker)
		thread_pool.append(tr)

		# print(f"Counter before start of {tr.name}: {counter}")
		tr.start()

	# wait for tread to finish:
	for tr in thread_pool:
		tr.join()

	print(f'counter in threaded: {counter}')


if __name__ == "__main__":
	counter = 0
	start = time()
	lock = threading.Lock()
	# sequential()
	threaded()
	end = time()
	# print(f'Time: {end-start}')