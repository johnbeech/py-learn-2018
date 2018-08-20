import random

range = [1,2,3,4,5,6,7,8,9,10]
results = []

for r in range:
    results.append(random.randint(1,10*r))

for r in results:
    print("Result %d" % r)
