import time as time

def sum_multiples(n, limit):
    k = (limit-1)//n
    return n*k*(k+1)//2

start = time.time()

# method 1
# print(sum([i for i in range(1, 1000) if i%3==0 or i%5==0]))

# method 2
# sum_mult_3 = 0
# i = 1
# while i <= 1000//3:
#     sum_mult_3 += 3*i
#     i += 1

# sum_mult_5 = 0
# i = 1
# while i < 1000//5:
#     sum_mult_5 += 5*i
#     i += 1

# sum_mult_15 = 0
# i = 1
# while i <= 1000//15:
#     sum_mult_15 += 15*i
#     i += 1

# print(sum_mult_3 + sum_mult_5 - sum_mult_15)

# method 3
n = 1000
print(sum_multiples(3, n) + sum_multiples(5, n) - sum_multiples(15, n))

end = time.time()
print(end - start)