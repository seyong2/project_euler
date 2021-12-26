import time as time
start = time.time()

solution = list()
triangles = list()
pentagonals = list()
hexagonals = list()

def triangle(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

i = 1
while len(solution) < 3:
    triangles.append(triangle(i))
    pentagonals.append(pentagonal(i))
    hexagonals.append(hexagonal(i))
    if triangle(i) in pentagonals and triangle(i) in hexagonals:
        solution.append(triangle(i))
    i += 1

end = time.time()
print(solution[-1])
print(end - start)
