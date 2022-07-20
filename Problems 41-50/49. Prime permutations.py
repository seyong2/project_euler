import time as time
import numpy as np

def is_prime(n):
    if (n in [0, 1]) or (n%2 == 0):
        return False
    elif n in [2, 3]:
        return True
    else:
        for d in range(2, int(n**0.5)+1):
            if n%d == 0:
                return False
                break
        return True

def perm_n(l, n):
    if n == 0:
        return [[]]
    else:
        perms = []
        for i in range(0, len(l)):
            temp = l[:] # copy
            a = temp[i]
            temp.remove(a)
            remain_combi = perm_n(temp, n-1)
            for j in remain_combi:
                perms.append((a, *j))
        return perms

def combi_n(l, n):
    if n == 0:
        return [[]]
    else:
        combis = []
        for i in range(0, len(l)):
            a = l[i]
            remain = l[i+1:]
            remain_combi = combi_n(remain, n-1)
            for j in remain_combi:
                combis.append((a, *j))
        return combis
    
tic = time.time()

results = list()

for i in range(1000, 10000):
    result = ''
    # check whether the number is prime or not
    if is_prime(i) == True:
        # if it's prime, create an empty list
        primes = list()
        # make a list of permutations using the digits of the number
        for j in perm_n(list(str(i)), 4):
            # we check whether the digit '0' comes first (we don't want 0123)
            # we also don't want the last digit is '0' because it's not prime.
            if (j[0] != '0') and (j[-1] != '0'):
                # we join the digits altogether
                number = ''.join(j)
                # check whether the joined number is prime or not
                # if it's prime, we include that number in the list
                # the second condition is for the cases where there are two same digits
                if (is_prime(int(number))) and (int(number) not in primes):
                    primes.append(int(number))
        for l in combi_n(primes, 3):
            l = sorted(l)
            if l[1] == (l[0]+l[2])/2:
                for m in l:
                    result += str(m)
                if int(result) not in results:
                    results.append(int(result))                

toc = time.time()
print(results)
print(toc - tic)
                        
                    
                    
            