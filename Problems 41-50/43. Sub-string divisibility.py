import time as time
from itertools import permutations
tic = time.time()

result = 0
digits = list(range(1, 10))
div = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17}
for i in list(permutations(digits, len(digits))):
    number = ''
    for j in i:
        number += str(j)
    for k in range(1, 10):
        number_temp = number[:k] + str(0) + number[k:]
        count = 0
        for m, n in div.items():
            if int(number_temp[m:m+3])%n == 0:
                count += 1
        if count == len(div):
            result += int(number_temp)
        
toc = time.time()
print(result)
print(toc - tic)
