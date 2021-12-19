import math
import time as time
start = time.time()

# define a function to determine a number is prime or not
def prime(number):
    if (number in [0, 1]) or (number % 2 == 0):
        return False
    elif number in [2, 3]:
        return True
    else:
        division_count = 0
        for i in range(2, math.ceil(number**0.5)):
            if number % i == 0:
                division_count += 1
        if division_count == 0:
            return True
        else: 
            return False

solution = 0
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(1, 10):
    minimum = ''.join(digits[:i])
    maximum = minimum[::-1]
    for j in range(int(minimum), int(maximum)+1):
        if sorted([d for d in str(j)]) != digits[:i]:
            continue
        else:
            if prime(j) == True:
                if j > solution:
                    solution = j
        
end = time.time()
print(solution) # 7652413
print(end - start)