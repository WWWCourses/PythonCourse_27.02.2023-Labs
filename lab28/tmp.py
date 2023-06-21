import threading
from typing import Any
from time import sleep, time

class CubThread(threading.Thread):
	def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, daemon=None) :
		super().__init__(group, target, name, args, kwargs, daemon=daemon)
		self.value = None


	def run(self):
		print(f'{self.name} is running')
		# super().run()

		self.value = self._target(*self._args, **self._kwargs)
		print(f'*********self.value in join: {self.value}')

		# print(f'self._target:{self._target}')
		# print(f'self._args:{self._args}')

	def join(self):
		super().join()
		return self.value

def cub(x):
	sleep(1)
	res = x**3
	print(f'{x}**3=={res}')
	return x**3


start = time()

# res1 = cub(2) # positional arg
# res2 = cub(x=3) # keyword arg
# print(res1+res2)

tr1 = CubThread(target=cub, args=(2,))
tr2 = CubThread(target=cub, kwargs={'x':3})

tr1.start()
tr2.start()
res1 = tr1.join()
res2 = tr2.join()

print(res1+res2)

end = time()
print(f'Time: {end-start}')






