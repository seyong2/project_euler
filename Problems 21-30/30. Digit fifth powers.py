import time as time

start = time.time()

numbers = [] # numbers that can be written as the sum of fifth powers of their digits

for n in list(range(2, 10**6)): # from 2 to 99999 as 1 cannot be included
    sum_of_fifth_powers = 0 # set the sum of fifth powers of n's digits
    for i in str(n): # transform n into string to loop over the digits
        sum_of_fifth_powers += int(i)**5 
    if sum_of_fifth_powers == n: 
        numbers.append(n)

end = time.time()
print(sum(numbers))
print(end - start)
