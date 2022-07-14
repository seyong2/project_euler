import time as time

with open("p067_triangle.txt") as f:
    lines = f.readlines()

tic = time.time()

for i in range(len(lines)):
    lines[i] = [int(j) for j in lines[i].strip('\n').split(' ')]
    
for i in range(len(lines)-1, 0, -1):
    down = lines[i]
    top = lines[i-1]
    for j in range(i):
        if down[j] > down[j+1]:
            lines[i-1][j] += down[j]
        else:
            lines[i-1][j] += down[j+1]

toc = time.time()
print(top[j]) 
print(toc - tic)