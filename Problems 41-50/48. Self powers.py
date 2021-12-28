import time as time
start = time.time()

sum = 0
for i in range(1, 1001):
    sum += i**i

solution = int(str(sum)[-10:])
end = time.time()
print(solution)
print(end - start)