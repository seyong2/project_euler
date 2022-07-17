import time as time
tic = time.time()

# create Champernowne's constant
# we are interested in only some of the fractional parts indicated below
digit_list = [10**0, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6]
solution = 1
fraction = ''
i = 1
while len(fraction) < 10**6:
    fraction += str(i)
    for j in digit_list:
        if len(fraction) >= j:
            solution *= int(fraction[j-1])
            digit_list.remove(j)
        else:
            break
    i += 1

toc = time.time()
print(solution)
print(toc - tic)
    