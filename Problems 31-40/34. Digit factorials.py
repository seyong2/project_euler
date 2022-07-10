import time as time

def factorial(number):
    f = 1
    if number == 0:
        return f
    else:
        for i in range(1, number+1):
            f *= i
        return f

tic = time.time()

factorials = [factorial(i) for i in range(0, 10)]
i = 10
solution = 0

while i < 6*factorials[-1]:
    fact_sum = 0
    for j in str(i):
        fact_sum += factorials[int(j)]    
    if fact_sum == i:
        solution += i
    i += 1

toc = time.time()
print(solution)
print(toc - tic)