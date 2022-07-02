import time as time
from itertools import permutations

def perm_n(l, n):
    if n == 0:
        return [[]]
    else:
        perms = []
        for i in range(0, len(l)):
            temp = l[:]
            a = temp[i]
            temp.remove(a)
            remain_combi = perm_n(temp, n-1)
            for j in remain_combi:
                perms.append((a, *j))
        return perms
    
tic = time.time()

result = []

for i in range(1, 10):
    for j in perm_n(list(range(1, 10)), i):
        a = ""
        for k in j:
            a += str(k)
        a = int(a)
        for k in range(1, 10-len(j)):
            for l in perm_n([item for item in list(range(1, 10)) if item not in j], k):
                b = ""
                for m in l:
                    b += str(m)
                b = int(b)
                product = a*b
                if sorted(j+l+tuple(map(int, str(product)))) == list(range(1,10)):
                    if product not in result:
                        result.append(product)

toc = time.time()
print(sum(result)) # 45228
print(toc-tic)     