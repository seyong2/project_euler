import numpy as np
import time as time
start = time.time()

def prime_or_not(number):
    if number == 1:
        return False
    elif number%2 == 0:
        return False
    else:
        division = 0
        for i in np.arange(3, int(np.sqrt(number))+1):
            if number%i == 0:
                division += 1
        if division == 0:
            return True
        else:
            return False
        
coefficients = {}
for a in range(-999, 1000):
    for b in range(2, 1000):
        coefficients[(a,b)] = 0
        n = 0
        while True:
            q = n**2 + a*n + b
            if q < 0:
                n += 1
            else:
                if prime_or_not(q) == True:
                    coefficients[(a,b)] += 1
                    n += 1
                else:
                    break

max_coefficients = max(coefficients, key=coefficients.get)

end = time.time()
print(np.product(max_coefficients))
print(end-start)

    