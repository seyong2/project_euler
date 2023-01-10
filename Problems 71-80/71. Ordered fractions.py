import time as time
    
tic = time.time()

# Farey sequence is a sequence which is generated for order n. 
# The sequence has all rational numbers in range [0/0 to 1/1] sorted in 
# increasing order such that the denominators are less than or equal to n 
# and all numbers are in reduced forms (GCD of numerator and denominator is 1).
# Source : https://www.geeksforgeeks.org/farey-sequence/

# If a/b and c/d are neighbours in a Farey sequence, with a/b < c/d,
# then b*c - a*d = 1. Thus, if we know b, c, and d, a = (b*c-1)/d

for d in range(10**6, 1, -1): # start from 1,000,000 for d (denominator)
    if (3*d-1)%7 == 0: # given d, we check if the numerator (n) is integer.
        n = int((3*d-1)/7)
        print(n) # print the numerator
        break    

toc = time.time()
print(toc - tic)