import string
import time as time

alphabets = list(string.ascii_uppercase)

with open('p042_words.txt') as f:
    data = f.read().strip('"').split('","')

def is_int_zero_of_function(number):
    zero_of_function = (-1+(1+4*2*number)**0.5)/2
    if str(zero_of_function).split('.')[-1] == '0':
        return True

tic = time.time()

solution = 0

for word in data:
    word_value = 0
    for character in word:
        word_value += alphabets.index(character)+1
    if is_int_zero_of_function(word_value):
        solution += 1
                
toc = time.time()
print(solution)
print(toc - tic)              