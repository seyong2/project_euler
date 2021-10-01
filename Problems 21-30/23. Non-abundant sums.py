import time as time
import numpy as np
from itertools import combinations_with_replacement

start = time.time()

abundant = []
for number in range(2, 28124):
    # Get proper divisors
    divisors = [1] 
    for i in range(1, round(np.sqrt(number)+1), 1):
        if number%i == 0:
            if i not in divisors:
                if i != int(number/i):
                    divisors.extend([i, int(number/i)])
                else:
                    divisors.append(i)
    # Determine whether the number is abundant or not
    if sum(divisors) > number:
        abundant.append(number)

# List of two abundant numbers
sum_of_two_abundants = []
combis = combinations_with_replacement(abundant, 2)
for combi in combis:
        sum_of_two_abundants.append(sum(list(combi)))

# Find the numbers that cannot be written as the sum of two numbers and add them up
answer = sum(set(range(1,28124)) - set(sum_of_two_abundants))
end = time.time()
print(answer)
print(end - start)
