import numpy as np
import time as time
start = time.time()
n = 20
grid = np.ones(shape = (n+1, n+1), dtype = np.int64)

for r in np.arange(1, n+1):
    for c in np.arange(1, n+1):
        grid[r, c] = grid[r, c-1] + grid[r-1, c]
        
print(np.max(grid))
end = time.time()
print(end - start)