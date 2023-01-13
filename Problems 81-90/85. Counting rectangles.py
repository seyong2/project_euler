# the total number of rectangles in a rectangular grid measuring by n_col by n_row 
# n_rectangles = (n_row*(n_row+1)/2)*(n_col*(n_col+1)/2)
import time as time

tic = time.time()

nm_combis = {}
n_row = 1    

while True:
    v = (8*10**6)/(n_row**2+n_row) # (4*2,000,000)/(n**2+n)
    n_col = 1 # we have to obtain a value for m such that the number of rectangles is closest to 2,000,000
    min_diff = v
    while True:
        diff = abs(n_col**2+n_col - v)
        if diff < min_diff:
            min_diff = diff
            nm_combis[n_row] = n_col
            n_col += 1
        else:      
            break
    n_row += 1
    if n_row >= n_col:
        break

differences = {}
for i, j in nm_combis.items():
    n_rectangles = (i*(i+1)/2)*(j*(j+1)/2)
    differences[(i, j)] = abs(n_rectangles - 2*10**6)    

toc = time.time()
print(min(differences, key=differences.get))
print(toc - tic)