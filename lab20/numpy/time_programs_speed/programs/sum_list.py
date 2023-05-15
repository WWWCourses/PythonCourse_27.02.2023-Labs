SIZE = 9_000_0000
arr = []
sum = 0

# Initialize list
for i in range(SIZE):
    arr.append(i)

# Calculate sum
for i in range(SIZE):
    sum += arr[i]

print(sum)

