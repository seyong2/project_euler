import csv
import time as time
start = time.time()

solution = 0
alphabets = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
             'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
             'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
with open('p042_words.txt') as f:
    for words in csv.reader(f):
        for word in words:
            word_value = 0
            for character in word:
                word_value += alphabets[character]
            n = 1
            while True:
                triangle_number = 0.5*n*(n+1)
                if triangle_number == word_value:
                    solution += 1
                elif triangle_number > word_value:
                    break
                n += 1
                
end = time.time()
print(solution)
print(end - start)              

