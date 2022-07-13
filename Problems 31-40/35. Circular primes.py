import time as time

def is_prime(number):
    if number == 1:
        return False
    elif number in [2, 3]:
        return True
    elif number%2 == 0:
        return False
    else:
        division = 0
        for i in range(2, int(number**(1/2))+1):
            if number%i == 0:
                division += 1
        if division == 0:
            return True
        else:
            return False
        
tic = time.time()
            
circular_primes = []
num_list = [2] + list(range(3, 10**6, 2)) # 2 + odd numbers

for i in num_list:
    # check whether i is prime or not
    if is_prime(i):
        # check whether i is alrealdy in the list of circular primes
        if i not in circular_primes:
            # create a list of digits
            digits = list(str(i))
            # check whether i is 2 or digits contains even numbers
            if (i == 2) or (0 not in [int(n)%2 for n in digits]):
                circular  =  [i]
                prime_number = 1
                t = 1
                while True:
                    digits += [digits.pop(0)]
                    c = ''.join(digits)
                    if int(c) != i:
                        if is_prime(int(c)):
                            prime_number += 1
                            circular.append(int(c))
                        t += 1
                    else:
                        break
                if (len(set(digits)) == 1) or (prime_number == len(digits)):
                    circular_primes += circular

toc = time.time()
print(len(circular_primes))
print(toc - tic)

         
