from multiprocessing import Pool
import time

def worker(n):
  # for light work, the pool is not efficient, try with n**10
  return n**1000

if __name__ == '__main__':
  t =time.time()
  range_n = 100000

  # create the Pool:
  with Pool(processes=5) as p:
    result = p.map(worker, range(range_n))

  p.join()

  print("Pool took: ", time.time() - t)

  # serial processing:
  t = time.time()
  result = []
  for x in range(range_n):
    result.append(worker(x))
  # print("Result: ", result)
  print("Serial processing took: ", time.time() - t)