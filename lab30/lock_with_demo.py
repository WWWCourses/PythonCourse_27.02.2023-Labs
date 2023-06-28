import threading


def worker():
	global x
	# l.acquire()
	# x+=1
	# l.release()

	with l:
		x+=1


x = 1
l = threading.Lock()

tr = threading.Thread(target=worker)
tr.start()

print(x)


