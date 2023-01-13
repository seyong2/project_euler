import time as time

with open('C:/Users/rsy54/OneDrive/Project Euler/Problems 81-90/p081_matrix.txt') as f:
    matrix = [i.split(',') for i in f.read().split('\n')[:-1]]
    matrix = [list(map(int, row)) for row in matrix]

tic = time.time()

for i in range(1, 80):
    matrix[i][0] += matrix[i-1][0]
    for j in range(1, 80):
        #matrix[i][0] += matrix[i-1][0]
        matrix[0][j] += matrix[0][j-1]
        matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

toc = time.time()

print(matrix[-1][-1])
print(toc - tic)