import multiprocessing as mp
from ctypes import c_int

def worker():
	x.value+=1

	print(f'x in {mp.current_process().name} = {x}')

if __name__ == '__main__':
	# x = 0
	x = mp.Value(c_int, 0)

	processes = []

	# crate and start 3 processes:
	for _ in range(3):
		pr = mp.Process(target=worker)
		pr.start()
		processes.append(pr)

	# wait for processes to end:
	for pr in processes:
		pr.join()


	print(f'x in {mp.current_process().name} = {x.value}')
