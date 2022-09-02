import time as time

# a function that determines whether a number is irrational or not
def is_irrational(n):
    # if the square root of n is not integer, n is irrational
    if (n**0.5).is_integer() == False:
        return True
    else:
        return False
    
# a function that sums the first one hundred decimals of an irrational number
# using long division method: https://www.geeksforgeeks.org/square-root-of-2/
def decimal_digits_sum_100(n):
    # create an empty string that will store the first one hundred decimals
    digits = ''
    # determine a number between 0 and 9 whose square is smaller than n
    divisor = max([i for i in range(0, 10) if i**2 < n])
    digits += str(divisor)
    quotient = divisor
    # compute the remainder and multiply it by 100 for next calculation
    remainder = (n-divisor*quotient)*100
    
    # we repeat the loop until we get 100 decimals
    while len(digits) < 100:
        # we find the smallest number between 0 and 9 such that int(str(2*quotient)+str(j))*j < remainder
        digit = max([str(j) for j in range(0, 10) if int(str(2*quotient)+str(j))*j < remainder])
        divisor = int(str(2*quotient)+digit)
        quotient = int(digits+digit)
        remainder -= (divisor*int(digit))
        remainder *= 100
        digits += digit
    
    result = 0
    for dec in list(digits):
        result += int(dec)
    
    return result

tic = time.time()

digit_sums = 0

for i in range(1, 101):
    if is_irrational(i):
        digit_sums += decimal_digits_sum_100(i)

toc = time.time()
print(digit_sums)
print(toc - tic)