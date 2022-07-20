import time as time

def is_prime(n):
    if n in [0, 1]:
        return False
    elif n in [2, 3]:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(2, int(n**(1/2))+1):
            if n%i == 0:
                return False
                break
            else:
                continue
        return True

tic = time.time()

primes = [2]
results = []

n = 3
while True:
    if is_prime(n):
        primes.append(n)
        for i in range(0, len(primes)):
            sum_primes = sum(primes[i:])
            if (is_prime(sum_primes)) and (sum_primes not in results):
                results.append(sum_primes)
                break
        if max(sorted(results))>10**6:
            break
       
    n += 1

#results.sort()

toc = time.time()
print(sorted(results)[-2])
print(toc-tic)