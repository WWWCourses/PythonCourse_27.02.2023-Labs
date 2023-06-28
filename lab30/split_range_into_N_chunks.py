import math

# with recursion
def variant1(n, chunks_count):
	data = range(1, n+1)
	data_len = len(data)
	chunk_size = math.ceil(data_len / chunks_count)  # the size of each chunk, rounded up

	def get_chunk(data):
		if not data:
			return

		chunk = data[:chunk_size]

		print(chunk)
		get_chunk(data[chunk_size:])

	get_chunk(data)

# with slicing
def variant2(n, chunks_count):
	data = range(1, n+1)
	data_len = len(data)
	chunk_size = math.ceil(data_len / chunks_count)  # the size of each chunk, rounded up

	# 1,2,3,4,
	# 5,6,7,8,
	# 9,10
	for i in range(0, data_len, chunk_size):
		chunk = data[i:i+chunk_size]
		print(chunk)

# # just start, end
def variant3(n, chunks_count):
	chunk_size = math.ceil(n / chunks_count)  # the size of each chunk, rounded up
	last_chunk = chunks_count-1

	for i in range(chunks_count):
		start = 1 if i==0 else end


		end = start+chunk_size if i!=last_chunk else n+1

		print(start, end)

n = 10
chunks_count = 3



print(f'{"Variant 1:":*^50}')
variant1(n, chunks_count)

print(f'\n{"Variant 2:":*^50}')
variant2(n, chunks_count)

print(f'\n{"Variant 3:":*^50}')
variant3(n, chunks_count)
