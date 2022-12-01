import time as time
tic = time.time()

result = sum([i**i for i in range(1, 1001)])%10**10

toc = time.time()
print(result)
print(toc - tic)