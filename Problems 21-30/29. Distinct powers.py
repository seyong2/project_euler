import time as time

start = time.time()

a = list(range(2, 101)) # list of bases
b = list(range(2, 101)) # ;ist of powers

combinations = []
for i in a:
    for j in b:
        combinations.append(i**j)

end = time.time()
print(len(set(combinations))) # set() removes duplicates
print(end - start)
