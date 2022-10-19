import time as time
tic = time.time()

base = 2
exp = 7830457
digits = 10

print((28433*pow(base, exp, 10**digits)+1)%(10**digits))
toc = time.time()
print(toc-tic)