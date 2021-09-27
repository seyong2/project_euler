import time as time

start = time.time()

l = []

for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        l.append(i)
sum = 0
for j in l:
    sum += j
print(sum)

end = time.time()
print(end - start)