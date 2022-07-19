import time as time

result = 0
triangles = list()

def triangle(n):
    return n*(n+1)/2

def is_int_zero_of_function_pentagon(number):
    zero_of_function = (1+(1+4*3*2*number)**0.5)/(2*3)
    if str(zero_of_function).split('.')[-1] == '0':
        return True
    else:
        return False

def is_int_zero_of_function_hexagon(number):
    zero_of_function = (1+(1+4*2*number)**0.5)/(2*2)
    if str(zero_of_function).split('.')[-1] == '0':
        return True
    else:
        return False

tic = time.time()

i = 286

while result == 0:
    if is_int_zero_of_function_pentagon(triangle(i)) and is_int_zero_of_function_hexagon(triangle(i)):
        result = triangle(i)
    i += 1

toc = time.time()

print(result)
print(toc - tic)
