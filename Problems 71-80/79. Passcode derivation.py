import time as time

tic = time.time()

with open("C:/Users/Seyong Ryoo/OneDrive/Project Euler/Problems 71-80/p079_keylog.txt") as f:
    data = [i for i in f.read().split('\n') if i != '']

passcode = []

for i in data:
    idx_code = []
    for j in list(i):
        if j not in passcode:
            passcode.append(j)
        idx_code.append(passcode.index(j))
    if idx_code != sorted(idx_code):
        for m, n in zip(idx_code, sorted(idx_code)):
            if m > n:
                passcode.insert(n, passcode.pop(m))     

toc = time.time()
print(''.join(passcode))
print(toc - tic)