import time as time
start = time.time()

numerators = [3]
denominators = [2]

for i in range(1, 1000):
    den = numerators[i-1]+denominators[i-1]
    num = den + denominators[i-1]
    numerators.append(num)
    denominators.append(den)

result = 0

for i in range(len(numerators)):
    if len(str(numerators[i])) > len(str(denominators[i])):
        result += 1

end = time.time()
print(result)
print(end - start)