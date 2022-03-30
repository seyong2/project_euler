import time as time
start = time.time()

i = 1

while True:
    digits = sorted(list(map(int, str(2*i))))
    for m in range(3, 7):
        if sorted(list(map(int, str(m*i)))) != digits:
            break
    if m == 6:
        print(i)
        break
    else:
        i += 1

end = time.time()
print(end - start)