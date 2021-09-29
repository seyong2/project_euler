import time as time
start = time.time()
c = list(range(2, 1000000))
c.reverse
m = 0
l = 0
for n in c:
    chain = 1
    temp = n
    while True:
        if temp%2 != 0:
            temp = 3*temp + 1
            chain += 1
        else:
            temp = temp/2
            chain += 1
        if temp == 1: break
    if chain > l:
        l = chain
        m = n
print(m)
end = time.time()
print(end - start)