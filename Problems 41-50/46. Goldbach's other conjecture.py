import time as time
start = time.time()

# define a function that determines whether a number is a prime number or not.
def prime(number):
    if number in [0, 1]:
        return False
    elif number in [2, 3]:
        return True
    elif number % 2 == 0:
        return False
    else:
        division = 0
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                division += 1
        if division == 0:
            return True
        else:
            return False

# define a fuction to see wheter a number is odd composite.
def odd_composite(number):
    if (number % 2 != 0) and (prime(number) == False):
        i = 1
        while 2*(i**2) < number:
            temp = number - 2*(i**2)
            if prime(temp) == True:
                return True
                break
            i += 1
        return False

n = 3
while True:
    if odd_composite(n) == False: 
        break
    n += 2

end = time.time()         
print(n)
print(end - start)