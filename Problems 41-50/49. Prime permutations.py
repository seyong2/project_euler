import time as time

def is_prime(n):
    if n <= 3:
        return n > 1
    elif n%2 == 0 or n%3 == 0:
        return False
    else:
        for d in range(5, int(n**0.5)+1, 6):
            if n%d == 0 or n%(d+2) == 0:
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
                combis.append([a, *j])
        return combis
    
tic = time.time()

result = 0
i = 1848

while result == 0:
    # check whether the number is prime or not
    if is_prime(i) == True:
        # if it's prime, create an empty list
        primes = list()
        # make a list of permutations using the digits of the number
        for j in perm_n(list(str(i)), 4):
            # we check whether the digit '0' comes first (i.e., we don't want 0123)
            # we also don't want the last digit is '0' because it's not prime.
            if '0' not in [j[0], j[-1]]:
                # we join the digits altogether
                number = int(''.join(j))
                # check whether the joined number is prime or not.
                # if it's prime, we include that number in the list.
                # the second condition is for the cases where there are two same digits.
                if (is_prime(number)) and (number not in primes):
                    primes.append(number)
        for l in combi_n(primes, 3):
            l.sort()
            if l[1] == (l[0]+l[2])/2:
                result = int(''.join(map(str, l)))
                break
    i += 1

toc = time.time()
print(result)
print(toc - tic)
                        
                    
                    
            