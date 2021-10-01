import time as time
import numpy as np

start = time.time()

proper_divisors = {}

for i in np.arange(2, 10001):
    proper_divisors[i] = [1]
    if i % 2 == 0:
        j = 2
        for j in np.arange(2, i, 2):
            if i%j == 0:
                if j in proper_divisors[i]:
                    pass
                else:
                    proper_divisors[i].extend([j, i/j])
            else:
                continue
    else:
        for j in np.arange(3, i, 2):
            if i%j == 0:
                if j in proper_divisors[i]:
                    pass
                else:
                    proper_divisors[i].extend([j, i/j])
    sum = 0
    for element in proper_divisors[i]:
        sum += element
    proper_divisors[i] = sum
        
#print(proper_divisors)

amicables = []
for key1, val1 in proper_divisors.items():
    for key2, val2 in proper_divisors.items():
        if key1 == val2 and val1 == key2 and key1 != key2:
            #print(key1, key2)
            amicables.extend([key1, key2])
            if key1 not in amicables:
                amicables.extend([key1, key2])
            else:
                pass
print(amicables)

sum_amicables = 0
for n in amicables:
    sum_amicables += n

print(sum_amicables)

end = time.time()

print(end - start)     

            
        
        


