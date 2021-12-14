import time as time
start = time.time()

maximum = 0
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# no two and three digit numbers cannot create 9 digit numbers by concatenating products with 1,2,...

for n in range(9123, 9877):
    product_result = ''
    # we multiply only by 1 and 2 because multiplying the number by 1 gives four digit number and by 2, five digit number, which sums up to 9.
    for d in range(1, 3):
        product = n*d
        # we do not want the number that contains 0.
        if '0' not in str(product):
            for p in str(product):
                product_result += p
    if sorted(product_result) == digits:
        if int(product_result) > maximum:
            maximum = int(product_result)

end = time.time()
print(maximum)
print(end - start)            
        
        
        
            

