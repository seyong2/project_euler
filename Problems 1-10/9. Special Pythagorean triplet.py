import time as time

start = time.time()

answer = 1
for a in range(1, 501):
    for b in range(500, 500-a, -1):
        c = 1000-a-b
        if c**2 == a**2 + b**2:
            answer = a*b*c
            break
    if answer != 1:
        break

print(answer)
end = time.time()
print(end - start)