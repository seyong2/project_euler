import time as time
tic = time.time()

def prime(number):
    if number in [0,1]:
        return False
    elif number in [2,3]:
        return True
    elif number%2 == 0:
        return False
    else:
        division = 0
        for d in range(2, int(number**0.5)+1):
            if number%d == 0:
                division += 1
            else:
                continue
        if division == 0:
            return True
        else:
            return False

n = 23
truncatable_primes = list()  

while len(truncatable_primes)<11:
    if prime(n):
        if (int(str(n)[0]) in [2, 3, 5, 7]) and (int(str(n)[-1]) in [3, 7]):
            count = 0
            for i in range(1, len(str(n))):
                if prime(int(str(n/(10**i)).split('.')[0])) and prime(int(str(n/(10**i)).split('.')[-1])):
                    count += 1
            if count == len(str(n))-1:
                truncatable_primes.append(n)
    n += 2
                
    
toc = time.time()
print(sum(truncatable_primes))
print(toc-tic)
