import time as time

def factorial(number):
    f = 1
    if number == 0:
        return f
    else:
        for i in range(1,number+1):
            f = f*i
        return f

start = time.time()

i = 3
solutions = []
while i<10**7:
    digits = []
    string = str(i)
    for s in string:
        digits.append(s)
    factorial_sum = 0
    for d in digits:
        factorial_sum += factorial(int(d))
    if factorial_sum == i:
        solutions.append(i)
    i += 1

end = time.time()
print(sum(solutions))