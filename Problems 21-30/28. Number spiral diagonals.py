import time as time

start = time.time()

shape = 1001 # 1001 * 1001 spiral
end = shape**2 # the last number of the spiral
diagonals = [1] # the list of diagonal elements

i = 1
r = 2 # gap between diagonal elements
while True:
    t = 1
    while t<=4: # there are 4 diagonals in each layer of the spiral
        i += r
        diagonals.append(i)
        t += 1
    if diagonals[-1] == end: # stop when we reach the last number of the spiral
        break
    else:
        r += 2 # the gap increases by 2 when moving to next layer

end = time.time()
print(sum(diagonals))
print(end - start)        


        
    

