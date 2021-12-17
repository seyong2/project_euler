import time as time
start = time.time()

# create Champernowne's constant
fraction = ''
i = 1
while len(fraction) < 10**6:
    fraction += str(i)
    i += 1

# we are interested in only some of the fractional parts indicated below
digit_list = [10**0, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6]
solution = 1
for digit in digit_list:
    solution *= int(fraction[digit-1])

end = time.time()
print(solution)
print(end - start)
    