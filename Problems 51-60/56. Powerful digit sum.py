import time as time
start = time.time()

result = 0

for a in range(1, 101):
    for b in range(1, 101):
        digit_sum = sum(list(map(int, str(a**b))))
        if digit_sum >= result:
            result = digit_sum
            
end = time.time()
print(result)
print(end - start)
        
            
        