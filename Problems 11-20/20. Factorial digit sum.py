import numpy as np
import time as time
start = time.time()

# Compute 100!
n = 100
i = 1
product = 1
while i < 101:
    product = product * i
    i += 1

# Sum the digits in 100!
digits_list = [i for i in str(product)]

digit_sum = 0
for i in digits_list:
    digit_sum += int(i)

end = time.time()
print(digit_sum)
print(end - start)
