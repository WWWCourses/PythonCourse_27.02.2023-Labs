from threading import Thread, current_thread
from time import sleep


class CubTread(Thread):
	def __init__(self, group=None, target=None, name=None,
				 args=(), kwargs={}, Verbose=None):
		Thread.__init__(self, group, target, name, args, kwargs)

		# self.value will store the value we need from thread's target
		self.value = None
		# print(dir(self))

	def run(self):
		self.value = self._target(*self._args, **self._kwargs)

	def join(self):
		print(f'{self.name} res={self.value}')
		return self.value

def cub(x):
	sleep(1)
	return x**3


tr1 = CubTread(target=cub, args=(1,))
tr2 = CubTread(target=cub, args=(2,))

tr1.start(); tr2.start()
res1 = tr1.join()
res2 = tr2.join()

print(res1+res2)