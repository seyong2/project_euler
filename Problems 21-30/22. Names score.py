import time as time
start = time.time()

alphabet_score = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
                  "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, 
                  "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
                  "W": 23, "X": 24, "Y": 25, "Z":26}

with open('p022_names.txt', 'r') as file:
    data = file.read().split(',')

names = []
for name in data:
    names.append(name.replace('"', ''))
names_ordered = sorted(names)    

score = 0
for name in names_ordered:
    char_score = 0
    for char in name:
        char_score += alphabet_score[char]
    score += char_score * (names_ordered.index(name)+1)

end = time.time()
print(score)
print(end - start)