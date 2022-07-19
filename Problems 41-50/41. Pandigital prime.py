import time as time

# define a function to determine a number is prime or not
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

def perm_n(l, n):
    if n == 0:
        return [[]]
    else:
        perms = []
        for i in range(0, len(l)):
            temp = l[:]
            a = temp[i]
            temp.remove(a)
            remain_combi = perm_n(temp, n-1)
            for j in remain_combi:
                perms.append((a, *j))
        return perms

tic = time.time()

solution = 0
digits = [str(i) for i in range(9, 0, -1)]

i = 9
while solution == 0:
    for j in perm_n(digits[len(digits)-i:], i):
        k = ''.join(j)
        if is_prime(int(k)):
            solution = int(k)
            break
    i -= 1
        
toc = time.time()
print(solution) # 7652413
print(toc - tic)