import time as time

start = time.time()

n = range(2, 10**6)
n_chain = dict()

for i in n:
    temp = i
    count = 1
    while temp != 1:
        if temp in n_chain.keys():
            count += n_chain[temp] - 1
            break
        else:
            if temp%2 == 0:
                temp /= 2
            else:
                temp = 3*temp + 1
            count += 1
    n_chain[i] = count

print(max(n_chain, key=n_chain.get))

end = time.time()
print(end - start)