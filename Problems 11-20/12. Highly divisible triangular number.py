import numpy as np
import time as time
start = time.time()
    
triangle = 0
natural_number = 1
while True:
    triangle += natural_number
    natural_number += 1
    divisors = []
    for i in np.arange(1, np.sqrt(triangle)+1):
        if (triangle%i == 0) and (i not in divisors):
            divisors.extend([i, triangle/i])
        else:
            pass
    if len(divisors) > 500:
        print(triangle)
        break
    
end = time.time()
print(end - start)