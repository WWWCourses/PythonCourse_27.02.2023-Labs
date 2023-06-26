import multiprocessing
from time import time

def worker():
	# global counter
	counter = q.get()
	print(f'Q size: {q.qsize()}') # 0
	pr_name = multiprocessing.current_process().name

	for i in range(1_000_000):
		counter += 1

	q.put(counter) # 1
	print(f'counter in {pr_name}  = {counter}')




def sequential():
	for _ in range(5):
		worker()

	print(f'counter in sequential: {counter}')


def process_demo():
	# create some treads to count together:
	processes_pool = []

	for i in range(5):
		pr = multiprocessing.Process(target=worker)
		processes_pool.append(pr)

		# print(f"Counter before start of {pr.name}: {counter}")
		pr.start()

	# wait for process to finish:
	for pr in processes_pool:
		pr.join()

	counter = q.get()
	print(f'counter in {pr_name}  = {counter}')


if __name__ == "__main__":
	# counter = 0
	q = multiprocessing.Queue()
	q.put(0)
	print(f'Q size: {q.qsize()}') #

	pr_name = multiprocessing.current_process().name

	start = time()
	# sequential()
	process_demo()
	end = time()
	# print(f'Time: {end-start}')