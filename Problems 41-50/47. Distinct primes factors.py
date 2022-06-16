import time as time
tic = time.time()

# define a function that determines whether a number is prime or not.
def is_prime(number):
    if number in [0, 1]:
        return False
    elif number in [2, 3]:
        return True
    elif number%2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5)+1):
            if number%i == 0:
                return False
                break
            else:
                continue
        return True

results = []
n = 210 # the smallest number with 4 prime factors = 2*3*5*7 = 210

while True:
    factors = []
    div = 2
    temp = n
    while temp != 1:
        while temp%div == 0:
            if (is_prime(div)):
                factors.append(div)
                temp = temp/div
        div += 1
    if len(set(factors)) == 4:
        results.append(n)
        if len(results) >= 4:
            if (n-3 in results) and (results.index(n)-3 == results.index(n-3)):
                print(n-3)
                break
    n += 1
toc = time.time()
print(toc-tic)
# 134043
