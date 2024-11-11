import time as time

start = time.time()

limit = 4*(10**6)
a, b = 0, 1
answer = 0

while b < limit:
    if b % 2 == 0:
        answer += b
    a, b = b, a + b

end = time.time()
print(answer)
print(end-start)