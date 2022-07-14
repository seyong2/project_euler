import time as time

def palindrome_10(number):
    if number == int(str(number)[::-1]):
        return True
    else:
        return False

def palindrome_2(number):
    remainders = ''
    while number > 0:
        remainders += str(number%2)
        number //= 2
    if remainders == remainders[::-1]:
        return True
    else:
        return False

tic = time.time()

solution = 0
for n in range(1, 10**6):
    if palindrome_10(n):
        if palindrome_2(n):
            solution += n

toc = time.time()
print(solution)
print(toc - tic)
        