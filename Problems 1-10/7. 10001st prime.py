import time as time
start = time.time()
prime = [2, 3]
i = 1
while True:
    candidates = [6*i-1, 6*i+1]
    for x in candidates:
        if 0 not in [x%y for y in prime]:
            prime.append(x)
    if len(prime) == 10001:
        break
    i += 1     
    
print(max(prime))
end = time.time()
print(end-start)