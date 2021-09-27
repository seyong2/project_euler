import time as time

start = time.time()
n = 600851475143

i = 2
factor = []

while i <= n:
    while n%i == 0:
        n = n/i
        factor.append(i)
    if i == 2:
        i += 1
    else:
        i += 2

print(max(factor))
end = time.time()
print(end-start)

