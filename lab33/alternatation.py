import re

# TASK: how many dogs and cats are in next text:
text = 'my dog is the best. The cat is on the mat. Dogs loves meat. Cats are the best. Caterpilares are not'

### Variant 1 = bad
# rx_cats = re.compile(r'\bcats?\b', re.I)
# rx_dogs = re.compile(r'\bdogs?\b', re.I)


# cats_res = rx_cats.findall(text)
# dogs_res = rx_dogs.findall(text)

# print(cats_res,dogs_res)

### Variant 2: the best
# rx = re.compile(r'\bcats?\b|\bdogs?\b',re.I)
# rx = re.compile(r'\b(?:cat|dog)s?\b',re.I)
# res = rx.findall(text)
# print(res)




