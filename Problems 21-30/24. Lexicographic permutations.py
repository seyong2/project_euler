import math 
import time as time
start = time.time()

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

permutations = 0
solution = ''

order = 0
while len(solution)<10:
    for d in digits:
        if permutations + math.factorial(len(digits)-1) < 10**6:
            permutations += math.factorial(len(digits)-1)
        else:
            order = digits[digits.index(d)]
            solution += str(order) # paste
            break
    digits.remove(order)
    
end = time.time()
print(solution)
print(end-start)
 



        
            
