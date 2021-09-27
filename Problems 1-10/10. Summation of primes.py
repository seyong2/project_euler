import time as time
start = time.time()

primes = [2, 3]
i = 1
limit = 2000000
while True:
    if 6*i-1 < limit and 6*i+1 < limit:
        primes.extend([6*i-1, 6*i+1])
    elif 6*i-1 < limit and 6*i+1 >= limit:
        primes.append(6*i-1)
    else:
        break
    i += 1

temp = primes[:]
for j in temp[1:]:
    for p in temp[:primes.index(j)]:
        if j%p == 0:
            primes.remove(j)
            break
       
print(sum(primes))
end = time.time()
print(end - start)
    