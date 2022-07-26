import time as time

def is_int_zero_of_function(number):
    if (1+(1+4*3*2*number)**0.5)%(2*3) == 0:
        return True
    else:
        return False

tic = time.time()

result = 0
pentagons = []
m = 1

while result == 0:
    a = m*(3*m-1)//2
    pentagons.append(a)

    for i in range(len(pentagons)):
        b = pentagons[i]
        if is_int_zero_of_function(a+b) and is_int_zero_of_function(a-b):
            result = a-b
            break
    m += 1
                                        
toc = time.time()
print(result) # 5482660
print(toc - tic)   