import time as time
start = time.time()

length = []
for i in range(1, 1000):
    e = 0
    remains = []
    while True:
        r = (10**e)%i
        if r not in remains:
            remains.append((10**e)%i)
            e += 1
        else:
            length.append(len(remains))
            break
        
end = time.time()
print(max(length)+1)
print(end-start)

#https://wiki.mathnt.net/index.php?title=%EB%B6%84%EC%88%98%EC%99%80_%EC%88%9C%ED%99%98%EC%86%8C%EC%88%98