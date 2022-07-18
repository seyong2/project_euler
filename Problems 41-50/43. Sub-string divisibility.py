import time as time

def perm_n(l, n):
    if n == 0:
        return [[]]
    # when we want more than zero element
    else:
        # we create an empty list that we will append all possible permutations of n elements
        perms = []
        # iterate through the elements of the list
        for i in range(0, len(l)):
            temp = l[:] # copy
            # take one element
            a = temp[i]
            # the remaining elements of the list 
            temp.remove(a)
            # we find permutations that have n-1 elements
            remain_combi = perm_n(temp, n-1)
            for j in remain_combi:
                # * is for getting rid of parenthesis ()
                perms.append((a, *j))
        return perms

result = 0
digits = list(str(s) for s in range(0, 10))
div = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17}

tic = time.time()

for i in perm_n(digits, len(digits)):
    if i[0] != '0':
        number = ''.join(i)
        count = 0
        for m, n in div.items():
            if int(number[m:m+3])%n == 0:
                count += 1
        if count == len(div):
            result += int(number)
        
toc = time.time()
print(result)
print(toc - tic)
