import time as time
#from itertools import combinations

def is_prime(number):
    if number in [0, 1]:
        return False
    elif number == 2:
        return True
    elif number%2 == 0:
        return False
    else:
        for i in range(2, int(number**0.5)+1):
            if number%i == 0:
                return False
                break
        return True

def combi_n(l, n):
    if n == 0:
        return [[]]
    # when we want more than zero element
    else:
        # we create an empty list that we will append all possible combinations of n elements
        combis = []
        # iterate through the elements of the list
        for i in range(0, len(l)):
            # take one element
            a = l[i]
            # the remaining elements of the list 
            # this prevents us from having combinations that have the same elements but ordered differently
            remain = l[i+1:]
            # we find combinations that have n-1 elements
            remain_combi = combi_n(remain, n-1)
            for j in remain_combi:
                # # * is for getting rid of parenthesis ()
                combis.append((a, *j))
        return combis

tic = time.time()
solution = 0
n = 56005
while solution == 0:
    length = len(str(n))
    for i in range(1, length):
        for j in combi_n(range(length), i):
            n_list = list(str(n))
            count = 0
            primes = []
            for k in range(10):
                for l in j:
                    n_list[l] = str(k)
                replaced = ''.join(n_list)
                if replaced[0] != '0':
                    if is_prime(int(replaced)):
                        count += 1
                        primes.append(int(replaced))
            if count == 8:
                solution = min(primes)
    n += 2
                
toc = time.time()
print(solution)
print(toc - tic)