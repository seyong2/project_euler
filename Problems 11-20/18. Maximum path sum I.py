import numpy as np
import time as time

start = time.time()

t1 = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

t1 = t1.split("\n")

arr = np.zeros((len(t1), len(t1)), int)
   
for i in range(len(t1)):
    j = 0
    for element in t1[i].split():
        arr[i, j] = int(element)
        j += 1

for i in range(len(arr)-1, 0, -1):
    sums = []
    for j in range(i):
        a = arr[i,j]+arr[i-1,j]
        b = arr[i,j+1]+arr[i-1,j]
        if a > b:
            sums.append(a)
        else:
            sums.append(b)
    #arr[i-1, :sum(arr[i-1]!=0)] = np.array(sums)
    arr[i-1, :i] = np.array(sums)

end = time.time()
print(arr[0,0]) 
print(end - start)       
        
            
        
