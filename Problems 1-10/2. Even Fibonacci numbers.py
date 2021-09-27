import time as time

start = time.time()
fib = [1, 2]
i = 1
while max(fib) < 4000000:
    fib.append(fib[i-1]+fib[i])
    i += 1
    
sum = 0
for j in fib:
    if j%2 == 0:
        sum += j
    else:
        continue
print(sum)
end = time.time()
print(end-start)

