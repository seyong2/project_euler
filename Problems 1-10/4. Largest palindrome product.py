import time as time

start = time.time()
palindrome = []
x = list(range(100, 1000))
y = []
for i in x:
    for j in x:
        y.append(i*j)
y = list(set(y))
y.sort(reverse=True)

for i in y:
    cha = str(i)
    if len(cha) == 6:
        if cha[-1] != cha[0]:
            continue
        elif cha[-2] != cha[1]:
            continue
        elif cha[-3] != cha[2]:
            continue
        else :
            palindrome.append(i)
    else:
        if cha[-1] != cha[0]:
            continue
        elif cha[-2] != cha[1]:
            continue
        else:
            palindrome.append(i)
    if len(palindrome) == 1:
        break

print(*palindrome)
end = time.time()
print(end-start)

