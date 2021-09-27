import time as time
start = time.time()
# the sum of the squares of the first one hundered natural numbers
x = sum([i**2 for i in list(range(1, 101))])
# the square of the sum of the first one hundered natural numbers
y = sum(list(range(1, 101)))**2
print(y - x)
end = time.time()
print(end - start)
