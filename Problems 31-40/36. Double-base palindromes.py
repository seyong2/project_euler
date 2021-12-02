import time as time
start = time.time()
def palindrome_10(number):
    if number==int(str(number)[::-1]):
        return True
    else:
        return False

def palindrome_2(number):
    remainders = ''
    while number>0:
        remainders += str(number%2)
        number = number//2
    if int(remainders)==int(remainders[::-1]):
        return True
    else:
        return False

solution = 0
for n in range(1,10**6):
    if palindrome_10(n)+palindrome_2(n)==2:
        solution += n
    else:
        continue
end = time.time()
print(solution)
print(end-start)
        