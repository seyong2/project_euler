import time as time
import numpy as np
    
tic = time.time()
    
result = 1
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

for a in range(0, int(target/100)+1):
    if 100*a == target:
        result += 1
        break
    else:
        for b in range(0, int((target-100*a)/50)+1):
            if 100*a+50*b == target:
                result += 1
                break
            elif 100*a+50*b < target:
                for c in range(0, int((target-100*a+50*b)/20)+1):
                    if 100*a+50*b+20*c == target:
                        result += 1
                        break
                    elif 100*a+50*b+20*c < target:
                        for d in range(0, int((target-100*a+50*b+20*c)/10)+1):
                            if 100*a+50*b+20*c+10*d == target:
                                result += 1
                                break
                            elif 100*a+50*b+20*c+10*d < target:
                                for e in range(0, int((target-100*a+50*b+20*c+10*d)/5)+1):
                                    if 100*a+50*b+20*c+10*d+5*e == target:
                                        result += 1
                                        break
                                    elif 100*a+50*b+20*c+10*d+5*e < target:
                                        for f in range(0, int((target-100*a+50*b+20*c+10*d+5*e)/2)+1):
                                            if 100*a+50*b+20*c+10*d+5*e+2*f == target:
                                                result += 1
                                                break
                                            elif 100*a+50*b+20*c+10*d+5*e+2*f < target:
                                                for g in range(0, target-(100*a+50*b+20*c+10*d+5*e+2*f)+1):
                                                    coin_sum = np.array(coins).dot(np.array([g,f,e,d,c,b,a,0]))
                                                    if coin_sum == target:
                                                        result += 1
                                    
toc = time.time()
print(result)
print(toc - tic)

# Dynamic programming
# https://www.educative.io/answers/what-is-coins-sums
# create a list of length 201 with the first element equal to 1,
# which represents that there is only one way to make 0p.
result = [1] + [0]*target

# for each coin from the list coins, we compute how many ways the coin make each amount.
for coin in coins:
    for i in range(coin, len(result)):
        result[i] += result[i-coin]
    
print(result[-1])