l = [5,4,3,2,1]

def bubble_sort(l):
	n = len(l)-1
	for i in range(n):
		for j in range(n-i):
			print(f'Compare: {l[j]},{l[j+1]}')
			if l[j+1]<l[j]:
				l[j],l[j+1] = l[j+1],l[j]

		print(f'\tPass {i+1}: {l}')

	print(l)

bubble_sort(l)


input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# def bubble_sort_LoT(l):
# 	n = len(l)-1
# 	for i in range(n):
# 		for j in range(n-i):
# 			if l[j+1][1]<l[j][1]:
# 				l[j],l[j+1] = l[j+1],l[j]

# 				print(f'\tCurrent: {l}')

# 	print(l)

# bubble_sort_LoT(input_list)