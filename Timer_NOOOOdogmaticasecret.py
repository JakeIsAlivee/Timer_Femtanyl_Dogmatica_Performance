#for context, there is a really old project of mine that i forgot about half-way
#now we're completing it cuz its a cool idea

#the dogmatica scene is ass cuz its a thousand FUCKING lines but we dont talk about that :3

#new timer but its also bad and im not rewriting all of this from scratch



import time
import os


#DATE format:        XX.XX.XXXX
#TIME format:        XX:XX:XX


try:
    filefolder = os.path.dirname(os.path.realpath(__file__))
    slash = os.sep
    dateandtimefile_lines = open(filefolder+slash+'Date_And_Time.txt','r',encoding='utf-8').readlines()
except FileNotFoundError:
    try:
        import sys
        filefolder = os.path.dirname(os.path.realpath(sys.executable))
        slash = os.sep
        dateandtimefile_lines = open(filefolder+slash+'Date_And_Time.txt','r',encoding='utf-8').readlines()
    except FileNotFoundError:
        print('Date_And_Time.txt should be in the same dir as this timer. I dont see it')
        time.sleep(120)
        exit()

for i in range(0,len(dateandtimefile_lines)):
    try:
        if dateandtimefile_lines[i].lower()[0:13] == 'startingpoint':
            startingpointdate = dateandtimefile_lines[i+1][0:10]
            startingpointtime = dateandtimefile_lines[i+2][0:8]
        if dateandtimefile_lines[i].lower()[0:8] == 'deadline':
            deadlinedate = dateandtimefile_lines[i+1][0:10]
            deadlinetime = dateandtimefile_lines[i+2][0:8]
    except IndexError:
        print('The information placement in the file is wrong')
        time.sleep(120)
        exit()


months = {
    1: 31,
    2: 28, #29
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

try:
    spday = int(startingpointdate[0:2])
    spmonth = int(startingpointdate[3:5])
    spyear = int(startingpointdate[6:10])
except:
    print('StartingPoint_Date is wrong')
    time.sleep(120)
    exit()
try:
    sphour = int(startingpointtime[0:2])
    spminute = int(startingpointtime[3:5])
    spsecond = int(startingpointtime[6:8])
except:
    print('StartingPoint_Time is wrong')
    time.sleep(120)
    exit()
try:
    dlday = int(deadlinedate[0:2])
    dlmonth = int(deadlinedate[3:5])
    dlyear = int(deadlinedate[6:10])
except:
    print('Deadline_Date is wrong')
    time.sleep(120)
    exit()
try:
    dlhour = int(deadlinetime[0:2])
    dlminute = int(deadlinetime[3:5])
    dlsecond = int(deadlinetime[6:8])
except:
    print('Deadline_Time is wrong')
    time.sleep(120)
    exit()

if spmonth > 12 or spmonth < 1:
    print("You cant go above 12 and below 1 in StartingPoint_Date's months")
    time.sleep(120)
    exit()
if dlmonth > 12 or dlmonth < 1:
    print("You cant go above 12 and below 1 in Deadline_Date's months")
    time.sleep(120)
    exit()

if spmonth == 2 and spyear % 4 == 0:
    if spday > months[spmonth]+1 or spday < 1:
        print("You cant go above the number of days in the month you chose and below 1 in StartingPoint_Date's days")
        time.sleep(120)
        exit()
else:
    if spday > months[spmonth] or spday < 1:
        print("You cant go above the number of days in the month you chose and below 1 in StartingPoint_Date's days")
        time.sleep(120)
        exit()

if dlmonth == 2 and dlyear % 4 == 0:
    if dlday > months[dlmonth]+1 or dlday < 1:
        print("You cant go above the number of days in the month you chose and below 1 in Deadline_Date's days")
        time.sleep(120)
        exit()
else:
    if dlday > months[dlmonth] or dlday < 1:
        print("You cant go above the number of days in the month you chose and below 1 in Deadline_Date's days")
        time.sleep(120)
        exit()

if sphour > 23 or sphour < 0:
    print("You cant go above 23 and below 0 in StartingPoint_Time's hours")
    time.sleep(120)
    exit()
if dlhour > 23 or dlhour < 0:
    print("You cant go above 23 and below 0 in Deadline_Time's hours")
    time.sleep(120)
    exit()

if spminute > 59 or spminute < 0:
    print("You cant go above 59 and below 0 in StartingPoint_Time's minutes")
    time.sleep(120)
    exit()
if dlminute > 59 or dlminute < 0:
    print("You cant go above 59 and below 0 in Deadline_Time's minutes")
    time.sleep(120)
    exit()

if spsecond > 59 or spsecond < 0:
    print("You cant go above 59 and below 0 in StartingPoint_Time's seconds")
    time.sleep(120)
    exit()
if dlsecond > 59 or dlsecond < 0:
    print("You cant go above 59 and below 0 in Deadline_Time's seconds")
    time.sleep(120)
    exit()

DEADLINE_IS_HERE = False

while True:

    time1 = time.perf_counter_ns()

    daynow = time.strftime('%d')
    monthnow = time.strftime('%m')
    yearnow = time.strftime('%Y')

    hournow = time.strftime('%H')
    minutenow = time.strftime('%M')
    secondnow = time.strftime('%S')



    datenow = daynow+'.'+monthnow+'.'+yearnow
    timenow = hournow+':'+minutenow+':'+secondnow



    twsecond = 0
    twminute = 0
    twhour = 0

    twday = 0
    twmonth = 0
    twyear = 0



    twsecond = int(secondnow) - int(spsecond) + int(twsecond)
    if twsecond < 0:
        twsecond = 60 + int(twsecond)
        twminute = -1
        twsecond = str(twsecond)
    if len(str(twsecond)) != 2:
        twsecond = '0'+str(twsecond)
    else:
        twsecond = str(twsecond)

    twminute = int(minutenow) - int(spminute) + int(twminute)
    if twminute < 0:
        twminute = 60 + int(twminute)
        twhour = -1
        twminute = str(twminute)
    if len(str(twminute)) == 1:
        twminute = '0'+str(twminute)
    else:
        twminute = str(twminute)

    twhour = int(hournow) - int(sphour) + int(twhour)
    if twhour < 0:
        twhour = 24 + int(twhour)
        twday = -1
        twhour = str(twhour)
    if len(str(twhour)) == 1:
        twhour = '0'+str(twhour)
    else:
        twhour = str(twhour)

    twday = int(daynow) - int(spday) + int(twday)
    if twday < 0:
        if int(yearnow) % 4 == 0 and int(monthnow) == 2:
            twday = months[int(monthnow)]+1 + int(twday)
        else:
            twday = months[int(monthnow)] + int(twday)
        twmonth = -1
        twday = str(twday)
    if len(str(twday)) == 1:
        twday = '0'+str(twday)
    else:
        twday = str(twday)

    twmonth = int(monthnow) - int(spmonth) + int(twmonth)
    if twmonth < 0:
        twmonth = 12 + int(twmonth)
        twyear = -1
        twmonth = str(twmonth)
    if len(str(twmonth)) == 1:
        twmonth = '0'+str(twmonth)
    else:
        twmonth = str(twmonth)
    
    twyear = int(yearnow) - int(spyear) + int(twyear)
    if twyear < 0:
        twyear = 0 
        twyear = str(twyear)
    if len(str(twyear)) == 1:
        twyear = '000'+str(twyear)
    if len(str(twyear)) == 2:
        twyear = '00'+str(twyear)
    if len(str(twyear)) == 3:
        twyear = '0'+str(twyear)
    else:
        twyear = str(twyear)
    


    timewasteddate = twday+'.'+twmonth+'.'+twyear
    timewastedtime = twhour+':'+twminute+':'+twsecond





    tlsecond = 0
    tlminute = 0
    tlhour = 0
    
    tlday = 0
    tlmonth = 0
    tlyear = 0


    tlsecond = int(dlsecond) - int(secondnow) + int(tlsecond)
    if tlsecond < 0:
        tlsecond = 60 + tlsecond
        tlminute = -1
        tlsecond = str(tlsecond)
    if len(str(tlsecond)) == 1:
        tlsecond = '0'+str(tlsecond)
    else:
        tlsecond = str(tlsecond)

    tlminute = int(dlminute) - int(minutenow) + int(tlminute)
    if tlminute < 0:
        tlminute = 60 + tlminute
        tlhour = -1
        tlminute = str(tlminute)
    if len(str(tlminute)) == 1:
        tlminute = '0'+str(tlminute)
    else:
        tlminute = str(tlminute)

    tlhour = int(dlhour) - int(hournow) + int(tlhour)
    if tlhour < 0:
        tlhour = 24 + tlhour
        tlday = -1
        tlhour = str(tlhour)
    if len(str(tlhour)) == 1:
        tlhour = '0'+str(tlhour)
    else:
        tlhour = str(tlhour)

    tlday = int(dlday) - int(daynow) + int(tlday)
    if tlday < 0:
        if int(yearnow) % 4 == 0 and int(monthnow) == 2:
            tlday = months[int(monthnow)]+1 + int(tlday) - 1
        else:
            tlday = months[int(monthnow)] + int(tlday) - 1
        tlmonth = -1
        tlday = str(tlday)
    if len(str(tlday)) == 1:
        tlday = '0'+str(tlday)
    else:
        tlday = str(tlday)

    tlmonth = int(dlmonth) - int(monthnow) + int(tlmonth)
    if tlmonth < 0:
        tlmonth = 12 + int(tlmonth)
        tlyear = -1
        tlmonth = str(tlmonth)
    if len(str(tlmonth)) == 1:
        tlmonth = '0'+str(tlmonth)
    else:
        tlmonth = str(tlmonth)

    tlyear = int(dlyear) - int(yearnow) + int(tlyear)
    if tlyear < 0:
        DEADLINE_IS_HERE = True
        tlyear = 0
        tlyear = str(tlyear)
    if len(str(tlyear)) == 1:
        tlyear = '000'+str(tlyear)
    if len(str(tlyear)) == 2:
        tlyear = '00'+str(tlyear)
    if len(str(tlyear)) == 3:
        tlyear = '0'+str(tlyear)
    else:
        tlyear = str(tlyear)

    

    timeleftdate = tlday+'.'+tlmonth+'.'+tlyear
    timelefttime = tlhour+':'+tlminute+':'+tlsecond



    totaltwdays = float(twyear) * 12
    totaltwdays = totaltwdays * 30.4375
    totaltwdays = float(twmonth) * 30.4375 + totaltwdays
    totaltwdays = totaltwdays + float(twday)
    totaltwdays = float(twhour) / 24 + totaltwdays
    totaltwdays = float(twminute) / 60 / 24 + totaltwdays
    totaltwdays = float(twsecond) / 60 / 60 / 24 + totaltwdays
    totaltwdays = round(totaltwdays, 5)
    totaltwdays = str(totaltwdays)

    totaltwmonths = float(totaltwdays) / 30.4375
    totaltwmonths = round(totaltwmonths, 7)
    totaltwmonths = str(totaltwmonths)

    totaltwyears = float(totaltwmonths) / 12
    totaltwyears = round(totaltwyears, 8)
    totaltwyears = str(totaltwyears)

    totaltwhours = float(totaltwdays) * 24
    totaltwhours = round(totaltwhours, 4)
    totaltwhours = str(totaltwhours)

    totaltwminutes = float(totaltwdays) * 24 * 60
    totaltwminutes = round(totaltwminutes, 3)
    totaltwminutes = str(totaltwminutes)

    totaltwseconds = float(totaltwdays) * 24 * 60 * 60
    totaltwseconds = round(totaltwseconds, 0) 
    totaltwseconds = str(totaltwseconds)


    totaltldays = float(tlyear) * 12
    totaltldays = totaltldays * 30.4375
    totaltldays = float(tlmonth) * 30.4375 + totaltldays
    totaltldays = totaltldays + float(tlday)
    totaltldays = float(tlhour) / 24 + totaltldays
    totaltldays = float(tlminute) / 60 / 24 + totaltldays
    totaltldays = float(tlsecond) / 60 / 60 / 24 + totaltldays
    totaltldays = round(totaltldays, 5)
    totaltldays = str(totaltldays)

    totaltlmonths = float(totaltldays) / 30.4375
    totaltlmonths = round(totaltlmonths, 7)
    totaltlmonths = str(totaltlmonths)

    totaltlyears = float(totaltlmonths) / 12
    totaltlyears = round(totaltlyears, 8)
    totaltlyears = str(totaltlyears)

    totaltlhours = float(totaltldays) * 24
    totaltlhours = round(totaltlhours, 4)
    totaltlhours = str(totaltlhours)

    totaltlminutes = float(totaltldays) * 24 * 60
    totaltlminutes = round(totaltlminutes, 3)
    totaltlminutes = str(totaltlminutes)

    totaltlseconds = float(totaltldays) * 24 * 60 * 60
    totaltlseconds = round(totaltlseconds, 0) 
    totaltlseconds = str(totaltlseconds)




    #dates length are 10 symbols
    #times length are 8 symbols

    #all first infos are 34 symbols long

    firstline =      'Starting point (date) = '+startingpointdate+     '  |  '+'Time WASTED:'+'\n'
    secondline =     'Starting point (time) = '+startingpointtime+'  '+'  |  '+'Years = = '+totaltwyears+'\n'
    thirdline =      'Deadline (date) = = = = '+deadlinedate+          '  |  '+'Months  = '+totaltwmonths+'\n'
    fourthline =     'Deadline (time) = = = = '+deadlinetime+     '  '+'  |  '+'Days  = = '+totaltwdays+'\n'
    fifthline =      '                                  '+             '  |  '+'Hours = = '+totaltwhours+'\n'
    sixthline =      'Time wasted (date)  = = '+timewasteddate+        '  |  '+'Minutes = '+totaltwminutes+'\n'
    seventhline =    'Time wasted (time)  = = '+timewastedtime+   '  '+'  |  '+'Seconds = '+totaltwseconds+'\n'

    if DEADLINE_IS_HERE:
        eighthline =     'Time left (date)  = = = '+'ALLLL GONE'+          '  |  '+'Time LEFT:'+'\n'
        ninthline =      'Time left (time)  = = = '+'ALL GONE'+       '  '+'  |  '+'Years = = '+'NO TIME'+'\n'
        tenthline =      '                                  '+             '  |  '+'Months  = '+'NOTHINGGGG'+'\n'
        eleventhline =   'Time now (date) = = = = '+datenow+               '  |  '+'Days  = = '+'NOTHINGGGG'+'\n'
        twelfthline =    'Time now (time) = = = = '+timenow+          '  '+'  |  '+'Hours = = '+'NUH UH'+'\n'
        thirteenthline = '                                  '+             '  |  '+'Minutes = '+'ITS GONEEE'+'\n'
        fourteenthline = '                                  '+             '  |  '+'Seconds = '+'GONE'+'\n'
    else:
        eighthline =     'Time left (date)  = = = '+timeleftdate+          '  |  '+'Time LEFT:'+'\n'
        ninthline =      'Time left (time)  = = = '+timelefttime+     '  '+'  |  '+'Years = = '+totaltlyears+'\n'
        tenthline =      '                                  '+             '  |  '+'Months  = '+totaltlmonths+'\n'
        eleventhline =   'Time now (date) = = = = '+datenow+               '  |  '+'Days  = = '+totaltldays+'\n'
        twelfthline =    'Time now (time) = = = = '+timenow+          '  '+'  |  '+'Hours = = '+totaltlhours+'\n'
        thirteenthline = '                                  '+             '  |  '+'Minutes = '+totaltlminutes+'\n'
        fourteenthline = '                                  '+             '  |  '+'Seconds = '+totaltlseconds+'\n'


    allinfomessage = firstline+secondline+thirdline+fourthline+fifthline+sixthline+seventhline+eighthline+ninthline+tenthline+eleventhline+twelfthline+thirteenthline+fourteenthline


    time2 = time.perf_counter_ns() - time1
    time2 = time2 / 1000000000
    time3 = 1.0 - time2
    if time3 < 0:
        time3 = 0
    #задержка в миллисекундах. сколько миллисекунд требуется для осуществления всех строчек кода в этом бесконечном цикле

    os.system('cls')

    print(allinfomessage)

    time.sleep(time3)



    
