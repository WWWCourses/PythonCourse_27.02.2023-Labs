from time import sleep, time
import threading


tr_name =  threading.current_thread().name
print(f'{tr_name} starts')

start = time()
total_sum = 0

n = 10_000_000
def calc_sum_squares(start, end):
	tr_name =  threading.current_thread().name
	print(f'*********** {tr_name} is calculating sum of {start} to {end}')
	global total_sum

	# CPU bound
	total_sum += sum( map(lambda x:x**2, range(start, end)) )

	# IO bound
	# sleep(2)
	print(f'---- total_sum in {tr_name} = {total_sum}')


# casum_squares(n//2, n+1 )


tr1= threading.Thread(target=calc_sum_squares, name='TR1', args=(1, n//2), kwargs={}, daemon=None)
tr2= threading.Thread(target=calc_sum_squares, name='TR2', args=(n//2, n+1), kwargs={}, daemon=True)
tr1.start();
tr2.start();

# tr1.join()
print(f'TR1 finished [total_sum={total_sum}]')
# tr2.join()
print(f'TR2 finished [total_sum={total_sum}]')

end = time()
print(f'total_sum = {total_sum};\n Time: {end-start}')
print(f'{tr_name} ends')
lc_sum_squares(1, n//2)
# calc_