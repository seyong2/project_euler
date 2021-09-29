import time as time
start = time.time()

number = 2**1000
digit_list = list(map(int, str(number)))
sum = 0
for digit in digit_list:
    sum += digit
print(sum)
end = time.time()
