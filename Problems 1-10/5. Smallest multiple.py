import time as time
import pandas as pd
import numpy as np

start = time.time()
x = list(range(1,21))
zero = [0] * (len(x)-1)
df = pd.DataFrame(zero)
idx = list(range(2,21))
df['Index'] = idx
df.set_index('Index', inplace=True)
df = df.rename(columns={0:'Count'})

for n in x:
    i = 2
    while i <= n:
        count = 0
        while n%i == 0:
            n = n/i
            count += 1
        if count > df['Count'].loc[i]:
            df['Count'].loc[i] = count
        if i == 2:
            i += 1
        else:
            i += 2

print(np.prod(df.index ** df.Count))
end = time.time()
print(end-start)
