from time import sleep, time
import multiprocessing
import math


# pr_name =  multiprocessing.current_process().name
# print(f'{pr_name} starts')


def sequential(n, chunks_count):
	start_time = time()
	total_sum = 0

	def calc_sum_squares(start, end):
		nonlocal total_sum

		pr_name = multiprocessing.current_process().name
		# print(f'*********** {pr_name} is calculating sum of {start} to {end}')

		# CPU bound
		total_sum += sum( map(lambda x:x**2, range(start, end)) )

	chunk_size = math.ceil(n/chunks_count)
	last_chunk = chunks_count-1

	for i in range(chunks_count):
		start = 1 if i==0 else end
		end = start+chunk_size if i!=last_chunk else n+1
		calc_sum_squares(start, end)

	print(f'total_sum in sequential: {total_sum}')
	print(f'Time: {time()-start_time}')

def process_demo(n,chunks_count):
	start_time = time()

	def calc_sum_squares(start, end):
		total_sum = q.get()

		pr_name = multiprocessing.current_process().name
		# print(f'*********** {pr_name} is calculating sum of {start} to {end}')

		# CPU bound
		total_sum += sum( map(lambda x:x**2, range(start, end)) )

		# print(f'---- total_sum in {pr_name} = {total_sum}')
		q.put(total_sum)

	process_pool = []
	q = multiprocessing.Queue()
	q.put(0)

	for i in range(chunks_count):
		chunk_size = math.ceil(n/chunks_count)
		last_chunk = chunks_count - 1
		start = 1 if i==0 else end
		end = start+chunk_size if i!=last_chunk else n+1

		pr = multiprocessing.Process(target=calc_sum_squares, args=(start, end), kwargs={}, daemon=None)
		process_pool.append(pr)
		pr.start()

	# join processes
	for pr in process_pool:
		pr.join()

	total_sum = q.get()
	print(f'total_sum in process_demo: {total_sum}')
	print(f'Time: {time()-start_time}')

def mp_pool_demo(n, chunks_count):
	start_time = time()
	p = multiprocessing.Pool(processes=chunks_count)
	# TODO - HW


	print(f'Time: {time()-start_time}')

if __name__ == "__main__":
	n = 50_000_000
	chunks_count = 4

	process_demo(n, chunks_count)
	sequential(n, chunks_count)

