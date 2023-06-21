def add(*args):
    print(args)
    # print(f'The sum is: ')

# add(1)
# add(1,2)
# add(1,2,3)

def foo(f, args=()):
    # print(f)
    # print(args)
	f(*args)


# foo(add, (1,))
# foo(add, (1,2))
foo(add, (1,2,3))

