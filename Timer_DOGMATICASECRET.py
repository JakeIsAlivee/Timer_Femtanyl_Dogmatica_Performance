#for context, there is a really old project of mine and i forgot about half-way
#now we're completing it cuz its a cool idea

#the timer is ass rn, its old
#the dogmatica scene is also ass cuz its a thousand fucking lines but we dont talk about that :3

import time

import os




import DOGMATICA_SCENE


Months_leapyear = {
    1: 31,
    2: 29,
    3: 31, 
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
} 
Months = {
    1: 31,
    2: 28,
    3: 31, 
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
} 

date1day = int(19)
date1month = int(10)
date1year = int(2024)
date1hour = int(10)
date1minute = int(59)
date1second = int(0)

if len(str(date1day)) == 1:
    str_date1day = str('0'+str(date1day))
else:
    str_date1day = str(str(date1day))
    
if len(str(date1month)) == 1:
    str_date1month = str('0'+str(date1month))
else:
    str_date1month = str(str(date1month))

if len(str(date1year)) == 3:
    str_date1year = str('0'+str(date1year))
if len(str(date1year)) == 2:
    str_date1year = str('00'+str(date1year))
if len(str(date1year)) == 1:
    str_date1year = str('000'+str(date1year))
else:
    str_date1year = str(str(date1year))

if len(str(date1hour)) == 1:
    str_date1hour = str('0'+str(date1hour))
else:
    str_date1hour = str(str(date1hour))

if len(str(date1minute)) == 1:
    str_date1minute = str('0'+str(date1minute))
else:
    str_date1minute = str(str(date1minute))

if len(str(date1second)) == 1:
    str_date1second = str('0'+str(date1second))
else:
    str_date1second = str(str(date1second))



date1datetime_print = str_date1day+'.'+str_date1month+'.'+str_date1year+' '+str_date1hour+':'+str_date1minute+':'+str_date1second

while True:
    
    os.system('cls||clear')
    
    dayNOW = int(time.strftime('%d'))
    monthNOW = int(time.strftime('%m'))
    yearNOW = int(time.strftime('%Y'))

    hourNOW = int(time.strftime('%H'))
    minuteNOW = int(time.strftime('%M'))
    secondNOW = int(time.strftime('%S'))

        
        
    
    str_dayNOW = str(time.strftime('%d'))
    str_monthNOW = str(time.strftime('%m'))
    str_yearNOW = str(time.strftime('%Y'))

    str_hourNOW = str(time.strftime('%H'))
    str_minuteNOW = str(time.strftime('%M'))
    str_secondNOW = str(time.strftime('%S'))

    datetimeNOW_print = str(str_dayNOW+'.'+str_monthNOW+'.'+str_yearNOW+' '+str_hourNOW+':'+str_minuteNOW+':'+str_secondNOW)

    years_leftto_date1 = date1year - yearNOW
    months_leftto_date1 = date1month - monthNOW
    days_leftto_date1 = date1day - dayNOW
                 
    hours_leftto_date1 = date1hour - hourNOW
    minutes_leftto_date1 = date1minute - minuteNOW
    seconds_leftto_date1 = date1second - secondNOW
    
    

    if hours_leftto_date1 < 0:
        hours_leftto_date1 = 24 + date1hour - hourNOW
        days_leftto_date1 -=1
    
    if minutes_leftto_date1 < 0:
        minutes_leftto_date1 = 60 + date1minute - minuteNOW 
        hours_leftto_date1 -= 1
    
    if seconds_leftto_date1 < 0:
        seconds_leftto_date1 = 60 + date1second - secondNOW
        minutes_leftto_date1-=1
    
    if minutes_leftto_date1 < 0:
        minutes_leftto_date1 = 59 + date1minute - minuteNOW 
        hours_leftto_date1 -= 1
    
    if days_leftto_date1 < 0:
        if yearNOW / 4:
            days_leftto_date1 = Months_leapyear[monthNOW] + date1day - dayNOW
            months_leftto_date1 -=1
            
        else:
            days_leftto_date1 = Months[monthNOW] + date1day - dayNOW
            months_leftto_date1 -=1
            
    

            
            
    
    
    
    
    
    
    if len(str(days_leftto_date1)) == 1:
        str_days_leftto_date1 = str('0'+str(days_leftto_date1))
    else:
        str_days_leftto_date1 = str(days_leftto_date1)
    
    if len(str(months_leftto_date1)) == 1:
        str_months_leftto_date1 = str('0'+str(months_leftto_date1))
    else:
        str_months_leftto_date1 = str(str(months_leftto_date1))

    if len(str(years_leftto_date1)) == 3:
        str_years_leftto_date1 = str('0'+str(years_leftto_date1))
    if len(str(years_leftto_date1)) == 2:
        str_years_leftto_date1 = str('00'+str(years_leftto_date1))
    if len(str(years_leftto_date1)) == 1:
        str_years_leftto_date1 = str('000'+str(years_leftto_date1))
    else:
        str_years_leftto_date1 = str(str(years_leftto_date1))
    


    if len(str(hours_leftto_date1)) == 1:
        str_hours_leftto_date1 = str('0'+str(hours_leftto_date1))
    else:
        str_hours_leftto_date1 = str(str(hours_leftto_date1))

    if len(str(minutes_leftto_date1)) == 1:
        str_minutes_leftto_date1 = str('0'+str(minutes_leftto_date1))
    else:
        str_minutes_leftto_date1 = str(str(minutes_leftto_date1))

    if len(str(seconds_leftto_date1)) == 1:
        str_seconds_leftto_date1 = str('0'+str(seconds_leftto_date1))
    else:
        str_seconds_leftto_date1 = str(str(seconds_leftto_date1))




    date_leftto_date1_print = str(str_days_leftto_date1 + '.'+str_months_leftto_date1+'.'+str_years_leftto_date1)

    time_leftto_date1_print = str(str_hours_leftto_date1+':'+str_minutes_leftto_date1+':'+str_seconds_leftto_date1)

    print('Date today:\n' + datetimeNOW_print+'\n')
    print('Counting from:\n'+date1datetime_print+'\n')
    print('Time left:\n'+date_leftto_date1_print+' '+time_leftto_date1_print)
    

    days_leftto_date1 = 0
    years_leftto_date1 = 0
    months_leftto_date1 = 0

    hours_leftto_date1 = 11
    minutes_leftto_date1 = 59



    if days_leftto_date1 == 0 and years_leftto_date1 == 0 and months_leftto_date1 == 0 and hours_leftto_date1 == 11 and minutes_leftto_date1 < 60 and minutes_leftto_date1 > 0:
        
        DOGMATICA_SCENE.START(date_leftto_date1_print,time_leftto_date1_print,0)

    
    time.sleep(1)