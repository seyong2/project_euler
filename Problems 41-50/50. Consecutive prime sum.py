import time as time
tic = time.time()

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

primes = []
results = []

number = 1
while True:
    if is_prime(number):
        primes.append(number)
        for i in range(0, len(primes)):
            sum_primes = sum(primes[i:])
            if (is_prime(sum_primes)==True) and (sum_primes not in results):
                results.append(sum_primes)
                break
        if max(results)>10**6:
            break
    number += 1

results.sort()

toc = time.time()
print(results[-2])
print(toc-tic)