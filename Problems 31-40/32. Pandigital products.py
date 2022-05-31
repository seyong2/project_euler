import time as time
from itertools import permutations
tic = time.time()

result = []
for i in range(1, 10):
    for j in permutations(list(range(1, 10)), i):
        a = ""
        for k in j:
            a += str(k)
        a = int(a)
        for k in range(1, 10-len(j)):
            for l in permutations([item for item in list(range(1, 10)) if item not in j], k):
                b = ""
                for m in l:
                    b += str(m)
                b = int(b)
                product = a*b
                if sorted(j+l+tuple(map(int, str(product)))) == list(range(1,10)):
                    if product not in result:
                        result.append(product)

toc = time.time()
print(sum(result))
print(toc-tic)     
        
        