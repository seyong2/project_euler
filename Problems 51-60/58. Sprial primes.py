import time as time

def is_prime(n):
    if n in [0, 1]:
        return False
    elif n in [2, 3]:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
                break
            else:
                continue
        return True

tic = time.time()

layer = 1
num = 1
diagonals = [num]
primes = []

while True:
    count = 0
    while count != 4:
        num += 2*layer
        diagonals.append(num)
        count += 1
        if is_prime(num):
            primes.append(num)
    if len(primes)/len(diagonals) <= 0.1:
        break
    else:
        layer += 1
      
toc = time.time()
print(diagonals[-1]**0.5)
print(toc - tic)    