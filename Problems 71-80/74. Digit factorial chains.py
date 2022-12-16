import time as time

# compute the factorial of a number
def factorial(number):
    result = 1 if number in [0, 1] else number*factorial(number-1)
    return result

# compute the sum of the factorial of the digits of a number
def sum_of_factorials(number):
    return sum([factorial(int(i)) for i in list(str(number))])

# define a function that gives a list of permutations of list l
def perm(l, n):
    if n == 0:
        return [[]]
    else:
        perms = []
        for i in range(len(l)):
            temp = l[:]
            a = temp[i]
            temp.remove(a)
            remain_combi = perm(temp, n-1)
            for j in remain_combi:
                perms.append([a, *j])
        return perms
    
tic = time.time()

result = 0

i = 1
while i < 10**6:
    # create a chain with the starting number in it
    chain = [i]
    temp = i
    count = 1
    while True:
        term = sum_of_factorials(temp)
        if term not in chain:
            chain.append(term)
            count += 1
            temp = term
        else:
            break
    if count == 60:
        result += 1
    i += 1
        
toc = time.time()

print(result) # 402
print(toc - tic)
        