import time as time
start = time.time()

def prime(number):
    if number == 1:
        return False
    elif number in [2,3]:
        return True
    elif number%2 == 0:
        return False
    else:
        division = 0
        for i in range(2,int(number**(1/2))+1):
            if number%i == 0:
                division += 1
        if division == 0:
            return True
        else:
            return False
            
primes = []
for i in range(1, 1000000):
    if prime(i) == False:
        continue
    else:
        prime_number = 1
        digits = [s for s in str(i)]
        t = 1
        while True:
            digits += [digits.pop(0)]
            c = ''
            for d in digits:
                c += d
            if int(c)!=i:
                if prime(int(c))==True:
                    prime_number += 1
                t += 1
            else:
                break
        if (len(set(digits))==1) or (prime_number==len(digits)):
            primes.append(i)

end = time.time()
print(len(primes))
print(end-start)

         
