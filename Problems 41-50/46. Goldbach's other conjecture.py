import time as time

# define a function that determines whether a number is a prime number or not.
def is_prime(number):
    if number in [0, 1]:
        return False
    elif number in [2, 3]:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
                break
        return True

# define a fuction to see wheter a number is odd composite.
def odd_composite(number):
    if (number % 2 != 0) and (is_prime(number) == False):
        i = 1
        while 2*(i**2) < number:
            temp = number - 2*(i**2)
            if is_prime(temp):
                return True
                break
            i += 1
        return False

tic = time.time()

n = 35
while True:
    if odd_composite(n) == False: 
        break
    n += 2

toc = time.time()         
print(n)
print(toc - tic)