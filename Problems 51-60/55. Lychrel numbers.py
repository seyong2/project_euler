import time as time
start = time.time()

result = 0

for i in range(1, 10001):
    itr = 1
    temp = i
    while itr <= 50:
        temp = temp + int(str(temp)[::-1])
        if temp != int(str(temp)[::-1]):
            itr += 1
        else:
            break
    if itr == 51:
        result += 1

end = time.time()
print(result)
print(end - start)