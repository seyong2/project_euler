import time as time

start = time.time()

def feb_days(year):
    if year%4 == 0:
        if str(year)[-2:] == '00' and year%400 != 0:
            return 28
        else:
            return 29
    else:
        return 28
        
month_days = {1: 31, 2: 0, 3: 31, 4: 30, 5: 31, 6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

sundays = 0
sunday_date = 6
for year in range(1901, 2001):
    month_days[2] = feb_days(year)
    for index, days in enumerate(month_days.values(), 1):
        #print(year, index)
        if index != 1:
            if sunday_date+7 > month_days[index-1]:
                sunday_date -= month_days[index-1]
            else:
                pass
        else:
            if sunday_date+7 > month_days[12]:
                sunday_date -= month_days[12]
        while True:
            if sunday_date == 1:
                    sundays += 1
            if sunday_date+7 > days:
                break
            else:
                sunday_date += 7
                #print(sunday_date)
                
end = time.time()
print(sundays)
print(end - start)

        
    
    



