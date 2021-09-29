import numpy as np
import time as time 

start = time.time()
words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
100: 'onehundred', 1000: 'onethousand'}

count = 0

for n in np.arange(1, 1001):
    if n in words:
         count += len(words[n])
    else: # n does not belong to the dictionary 'words'
        s = list(map(int, str(n)))
        if len(s) == 2: # two digit number
            s[0] = s[0] * 10
            for i in s:
                count += len(words[i])
        else: # three digit number
            if (s[1] == 0 and s[-1] != 0): # e.g. 201
                s.remove(0) 
                count += len('hundred') + len('and')
                for i in s:
                    count += len(words[i]) 
            elif (s[1] != 0 and s[-1] == 0): # e.g. 210
                s[1] = s[1] * 10
                count += len('hundred') + len('and')
                for i in s[:-1]: # only the first two numbers of the list
                    count += len(words[i]) 
            elif (s[1] == 0 and s[-1] == 0):
                count += len(words[s[0]]) + len('hundred')
            else: # n does not contain 0
                if s[1] != 1: # e.g. 324
                    s[1] = s[1] * 10
                    count += len('hundred') + len('and')
                    for i in s:
                        count += len(words[i])
                else: # e.g. 215
                    s[1] = s[1] * 10 + s[-1]
                    count += len('hundred') + len('and')
                    for i in s[:-1]:
                        count += len(words[i])
                
print(count) # 21124

end = time.time()
print(end - start)
                
           
        

