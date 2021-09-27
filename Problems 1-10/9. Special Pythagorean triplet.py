import time as time

start = time.time()
count = 0
for a in range(1,501):
    for b in range(500,500-a,-1):
        c = 1000 - a - b
        if c**2 == a**2 + b**2:
            print(a*b*c)
            count += 1
            break
    if count == 1: break

end = time.time()
print(end - start)