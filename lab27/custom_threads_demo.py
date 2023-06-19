from collections.abc import Callable, Iterable, Mapping
from time import sleep, time
import threading
from typing import Any

class ResThread(threading.Thread)
	def __init__()

def worker(x):
    print(f'{threading.current_thread().name} is working...')
    sleep(0.5)
    res = x+1
    print(f'res = {res}')
    return res


# res1 = worker(1)
# res2 = worker(2)
# res3 = worker(3)

# tr1 =  threading.Thread(target=worker, args=(1,))
tr1 =  ResThread()
tr1.start(); tr1.join()
print(dir(tr1))

# print(f'Total res = {res1+res2+res3}')
