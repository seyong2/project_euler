import time as time
start = time.time()

def factorial(number):
    result = 1
    if number == 0:
        result *= 1
    else:
        for n in range(2, number+1):
            result *= n
    return result
    
result = 0

for n in range(1, 101):
    for r in range(1, n+1):
        if factorial(n)/(factorial(r)*factorial(n-r)) > 10**6:
            result += 1

end = time.time()            
print(result)
