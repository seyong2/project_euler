import time as time
import numpy as np
tic = time.time()

result = 0
digit = 1

while True:
    lower = 10**((digit-1)/digit)
    interval = range(int(np.ceil(lower)), 10)
    if len(interval) >= 1:
        for i in interval:
            result += 1
    else:
        break
    digit += 1
        
toc = time.time()
print(result)
print(toc - tic)