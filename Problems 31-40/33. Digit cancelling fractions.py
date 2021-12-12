import time as time
import numpy as np
start = time.time()

numerators = []
denominators = []

for n in range(10, 99):
    for d in range(n+1, 100):
        num_digits = set(str(n))
        den_digits = set(str(d))
        # if there is no common digits, then we continue with other numbers
        if len(num_digits.intersection(den_digits)) == 0:
            continue
        else:
            common_digits = list(num_digits.intersection(den_digits))
            # having 0 as common digit makes a trivial case
            if common_digits[0] != '0':  
                # we remove the common digit
                num_digits = list(str(n))
                den_digits = list(str(d))
                num_digits.remove(common_digits[0])
                den_digits.remove(common_digits[0])
                # having 0 in the denominator does not make any sense
                if int(den_digits[0]) != 0:
                    if n/d == int(num_digits[0])/int(den_digits[0]):
                        numerators.append(int(num_digits[0]))
                        denominators.append(int(den_digits[0]))
solution = np.prod(denominators)/np.prod(numerators)
end = time.time()
print(solution)
print(end-start)
