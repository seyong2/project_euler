import time as time

def num_to_roman(loc, n):
    if loc == 3:
        return 'M'*n
    elif loc == 2:
        if n < 4:
            return 'C'*n
        elif n == 4:
            return 'CD'
        elif n < 9:
            return ''.join('D'+'C'*(n-5))
        else:
            return 'CM'
    elif loc == 1:
        if n < 4:
            return 'X'*n
        elif n == 4:
            return 'XL'
        elif n < 9:
            return ''.join('L'+'X'*(n-5))
        else:
            return 'XC'
    elif loc == 0:
        if n < 4:
            return 'I'*n
        elif n == 4:
            return 'IV'
        elif n < 9:
            return ''.join('V'+'I'*(n-5)) 
        else:
            return 'IX'
    
tic = time.time()

with open("C:/Users/Seyong Ryoo/OneDrive/Project Euler/Problems 81-90/p089_roman.txt") as f:
    data = [i for i in f.read().split('\n')]
    
roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

roman_2_num = dict()
num_2_roman = []

for roman in data:
    n = 0
    i = 0
    while i < len(roman):
        if (roman[i] not in ['I', 'X', 'C']) or (i == len(roman)-1):
            n += roman_numerals[roman[i]]
            i += 1
        elif roman[i] in ['I', 'X', 'C']:
            if roman[i] == 'I':
                if roman[i+1] in ['V', 'X']:
                    n += roman_numerals[roman[i+1]] - roman_numerals[roman[i]]
                    i += 2
                else:
                    n += roman_numerals[roman[i]]
                    i += 1
            elif roman[i] == 'X':
                if roman[i+1] in ['L', 'C']:
                    n += roman_numerals[roman[i+1]] - roman_numerals[roman[i]]
                    i += 2
                else:
                    n += roman_numerals[roman[i]]
                    i += 1
            else:
                if roman[i+1] in ['D', 'M']:
                    n += roman_numerals[roman[i+1]] - roman_numerals[roman[i]]
                    i += 2
                else:
                    n += roman_numerals[roman[i]]
                    i += 1
                
    roman_2_num[roman] = n
    n_len = len(str(n))
    r = ''
    for j in range(n_len-1, -1, -1):
        r += num_to_roman(j, int(str(n)[::-1][j]))
    num_2_roman.append(r)

result = 0
for i in range(len(data)):
    result += len(data[i])-len(num_2_roman[i])

toc = time.time()
print(result)
print(toc - tic)