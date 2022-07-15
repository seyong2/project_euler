import time as time

def is_prime(number):
    if number in [0,1]:
        return False
    elif number in [2,3]:
        return True
    elif number%2 == 0:
        return False
    else:
        for d in range(2, int(number**0.5)+1):
            if number%d == 0:
                return False
                break
        return True

tic = time.time()

n = 23
truncatable_primes = list()  

while len(truncatable_primes) < 11:
    if is_prime(n):
        if (int(str(n)[0]) in [2, 3, 5, 7]) and (int(str(n)[-1]) in [3, 7]):
            count = 0
            for i in range(1, len(str(n))):
                if is_prime(n%(10**i)) and is_prime(n//(10**i)):
                    count += 1
            if count == len(str(n))-1:
                truncatable_primes.append(n)
    n += 2                
    
toc = time.time()
print(sum(truncatable_primes))
print(toc-tic)
