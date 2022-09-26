import time as time

tic = time.time()

cube_dict = dict()

i = 1

result = 0

while result == 0:
    cube = i**3
    digit_list = tuple(sorted(list(str(cube))))
    if digit_list not in list(cube_dict.keys()):
        cube_dict[digit_list] = [cube]
    else:
        cube_dict[digit_list].append(cube)
    for val in cube_dict.values():
        if len(val) == 5:
            result = min(val)
    i += 1

toc = time.time()        
print(result)
print(toc - tic)
