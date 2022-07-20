import time as time
tic = time.time()

sum_series = sum([i**i for i in range(1, 1001)])

toc = time.time()
print(int(str(sum_series)[-10:]))
print(toc - tic)