import subprocess
import random
import os
import datetime
import time
import math

startTime = time.time() 
subprocess.call(["cmd", "/c", "start", "/wait", "/max", "mx"])
endTime = time.time()
playTime = math.floor(endTime - startTime)

# dont keep records less than 1 minute
if playTime < 60:
    quit()




def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def secondsToString(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return "{0}:{1}:{2}".format(int(hours), int(mins), sec)

def stringToSeconds(str):
    array = str.split(':')
    hours = int(array[0])
    minutes = int(array[1])
    seconds = int(array[2])
    return (hours*60*60)+(minutes*60)+seconds

# test
# for x in range(0, 2000):
#     if(x % 5 == 0):
#         randString = secondsToString(x)
#         print(randString)
#         print(stringToSeconds(randString))


def getOldValues():
    with open("C:\\Users\Win 10 PC\Desktop\scripts\MxSim\mxStats\playTime.txt", "r") as f1:
        contents = f1.read()
        lines = contents.splitlines()
        column = 34

        timesPlayedTotal = lines[2][column:]
        timePlayedAllTime = stringToSeconds(lines[3][column:])
        avgplayTimePerSession = stringToSeconds(lines[4][column - 1:]) # idk...

        timePlayedThisDay = stringToSeconds(lines[6][column:])
        timePlayedThisWeek = stringToSeconds(lines[7][column:])
        timePlayedThisMonth = stringToSeconds(lines[8][column:])
        timePlayedThisYear = stringToSeconds(lines[9][column:])

        avgTimePlayedPerDay = stringToSeconds(lines[11][column:])
        avgTimePlayedPerWeek = stringToSeconds(lines[12][column:])
        avgTimePlayedPerMonth = stringToSeconds(lines[13][column:])
        avgTimePlayedPerYear = stringToSeconds(lines[14][column:])

        allTimeHighPlayedPerDay = stringToSeconds(lines[16][column:])
        allTimeHighPlayedPerWeek = stringToSeconds(lines[17][column:])
        allTimeHighPlayedPerMonth = stringToSeconds(lines[18][column:])
        allTimeHighPlayedPerYear = stringToSeconds(lines[19][column:])

        timesPlayedThisDay = lines[23][column:]
        timesPlayedThisWeek = lines[24][column:]
        timesPlayedThisMonth = lines[25][column:]
        timesPlayedThisYear = lines[26][column:]

        avgTimesPlayedThisDay = lines[28][column:] ## change name to per day
        avgTimesPlayedThisWeek = lines[29][column:]
        avgTimesPlayedThisMonth = lines[30][column:]
        avgTimesPlayedThisYear = lines[31][column:]

        athTimesPlayedPerDay = lines[33][column:]
        athTimesPlayedPerWeek = lines[34][column:]
        athTimesPlayedPerMonth = lines[35][column:]
        athTimesPlayedPerYear = lines[36][column:]

        lastUpdated = lines[38][column:]
        docCreated =lines[39][column:]

        pObject = {
                   'timesPlayedTotal': int(timesPlayedTotal),
                   'timePlayedAllTime': timePlayedAllTime,
                   'avgplayTimePerSession': avgplayTimePerSession,

                   'timePlayedThisDay': timePlayedThisDay,
                   'timePlayedThisWeek': timePlayedThisWeek,
                   'timePlayedThisMonth': timePlayedThisMonth,
                   'timePlayedThisYear': timePlayedThisYear,

                   'avgTimePlayedPerDay': avgTimePlayedPerDay,
                   'avgTimePlayedPerWeek': avgTimePlayedPerWeek,
                   'avgTimePlayedPerMonth': avgTimePlayedPerMonth,
                   'avgTimePlayedPerYear': avgTimePlayedPerYear,

                   'allTimeHighPlayedPerDay': allTimeHighPlayedPerDay,
                   'allTimeHighPlayedPerWeek': allTimeHighPlayedPerWeek,
                   'allTimeHighPlayedPerMonth': allTimeHighPlayedPerMonth,
                   'allTimeHighPlayedPerYear': allTimeHighPlayedPerYear,

                   'timesPlayedThisDay': float(timesPlayedThisDay),
                   'timesPlayedThisWeek': float(timesPlayedThisWeek),
                   'timesPlayedThisMonth': float(timesPlayedThisMonth),
                   'timesPlayedThisYear': float(timesPlayedThisYear),

                   'avgTimesPlayedThisDay': float(avgTimesPlayedThisDay),
                   'avgTimesPlayedThisWeek': float(avgTimesPlayedThisWeek),
                   'avgTimesPlayedThisMonth': float(avgTimesPlayedThisMonth),
                   'avgTimesPlayedThisYear': float(avgTimesPlayedThisYear),

                   'athTimesPlayedPerDay': float(athTimesPlayedPerDay),
                   'athTimesPlayedPerWeek': float(athTimesPlayedPerWeek),
                   'athTimesPlayedPerMonth': float(athTimesPlayedPerMonth),
                   'athTimesPlayedPerYear': float(athTimesPlayedPerYear),

                   'docCreated': docCreated,
                   'lastUpdated': lastUpdated,
                   }
    return pObject

values = getOldValues()

docCreated = values['docCreated']
lastUpdated = values['lastUpdated']

docCreatedObj = datetime.datetime.strptime(docCreated, '%Y-%m-%d')
lastUpdatedObj = datetime.datetime.strptime(lastUpdated, '%Y-%m-%d')
currentDateObj = datetime.datetime.now()

startToLastDelta = lastUpdatedObj - docCreatedObj
startToNowDelta = currentDateObj - docCreatedObj 
lastToNowDelta = currentDateObj - lastUpdatedObj


def updateDays():
    # timePlayedThisDay
    newTimePlayedThisDay = values['timePlayedThisDay'] + playTime if lastToNowDelta.days == 0 else playTime

    # avgTimePlayedPerDay
    newAvgTimePlayedPerDay = (values['avgTimePlayedPerDay'] * (startToLastDelta.days + 1) + playTime) / (startToNowDelta.days + 1)
    
    # athTimePerDay
    newAthTimePerDay = newTimePlayedThisDay if newTimePlayedThisDay > values['allTimeHighPlayedPerDay'] else values['allTimeHighPlayedPerDay']
   
    # timesPlayedThisDay
    newTimesPlayedThisDay = values['timesPlayedThisDay'] + 1 if lastToNowDelta.days == 0 else 1
    
    # avgTimesPlayedPerDay
    newAvgTimesPlayedThisDay = ((values['avgTimesPlayedThisDay'] * (startToLastDelta.days + 1)) + 1) / (startToNowDelta.days + 1)

    # athTimesPlayedPerDay
    newAthTimesPlayedPerDay = newTimesPlayedThisDay if newTimesPlayedThisDay > values['athTimesPlayedPerDay'] else values['athTimesPlayedPerDay']

    return{
    'newTimePlayedThisDay': secondsToString(newTimePlayedThisDay),
    'newAvgTimePlayedPerDay': secondsToString(int(newAvgTimePlayedPerDay)),
    'newAthTimePerDay': secondsToString(newAthTimePerDay),
    'newTimesPlayedThisDay': int(newTimesPlayedThisDay),
    'newAvgTimesPlayedThisDay': round(newAvgTimesPlayedThisDay, 5),
    'newAthTimesPlayedPerDay': int(newAthTimesPlayedPerDay),
    }


def updateWeeks():
    # create diff_week()
    startMonday = (docCreatedObj - datetime.timedelta(days=docCreatedObj.isoweekday()))
    lastUpdateMonday = (lastUpdatedObj - datetime.timedelta(days=lastUpdatedObj.isoweekday()))
    todayThing = (currentDateObj - datetime.timedelta(days=currentDateObj.isoweekday()))

    startToLastUpdateWeeks = ((lastUpdateMonday - startMonday).days / 7)
    startToNowWeeks = ((todayThing - startMonday).days / 7)
    lastUpdateToNowWeeks = ((todayThing - lastUpdateMonday).days / 7)

    # print('startToLastUpdateWeeks:', startToLastUpdateWeeks)
    # print('startToNowWeeks:', startToNowWeeks)
    # print('lastUpdateToNowWeeks:', lastUpdateToNowWeeks)
    
    # timePlayedThisWeek
    newTimePlayedThisWeek = values['timePlayedThisWeek'] + playTime if lastUpdateToNowWeeks == 0 else playTime

    # avgTimePlayedPerWeek
    newAvgTimePlayedPerWeek = (values['avgTimePlayedPerWeek'] * (startToLastUpdateWeeks + 1) + playTime) / (startToNowWeeks + 1)

    # athTimePerWeek
    newAthTimePerWeek = newTimePlayedThisWeek if newTimePlayedThisWeek > values['allTimeHighPlayedPerWeek'] else values['allTimeHighPlayedPerWeek']

    # timesPlayedThisWeek
    newTimesPlayedThisWeek = values['timesPlayedThisWeek'] + 1 if lastUpdateToNowWeeks == 0 else 1

    newAvgTimesPlayedPerWeek = ((values['avgTimesPlayedThisWeek'] * (startToLastUpdateWeeks + 1)) + 1) / (startToNowWeeks + 1)

    # athTimesPlayedPerWeek 
    newAthTimesPlayedPerWeek = newTimesPlayedThisWeek if newTimesPlayedThisWeek > values['athTimesPlayedPerWeek'] else values['athTimesPlayedPerWeek']

    return{
    'newTimePlayedThisWeek': secondsToString(newTimePlayedThisWeek),
    'newAvgTimePlayedPerWeek': secondsToString(int(newAvgTimePlayedPerWeek)),
    'newAthTimePerWeek': secondsToString(newAthTimePerWeek),
    'newTimesPlayedThisWeek': int(newTimesPlayedThisWeek),
    'newAvgTimesPlayedPerWeek': round(newAvgTimesPlayedPerWeek, 5),
    'newAthTimesPlayedPerWeek': int(newAthTimesPlayedPerWeek),
    }

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def updateMonths():
    startToLastMonthsDiff = diff_month(lastUpdatedObj, docCreatedObj)
    startToNowMonthsDiff = diff_month(currentDateObj, docCreatedObj)
    lastUpdateToNowMonthsDiff = diff_month(currentDateObj ,lastUpdatedObj)

    
#   timePlayedThisMonth
    newTimePlayedThisMonth = values['timePlayedThisMonth'] + playTime if lastUpdateToNowMonthsDiff == 0 else playTime

#   avgTimePlayedPerMonth
    newAvgTimePlayedPerMonth = (values['avgTimePlayedPerMonth'] * (startToLastMonthsDiff + 1) + playTime) / (startToNowMonthsDiff + 1)

#   athTimePerMonth
    newAthTimePerMonth = newTimePlayedThisMonth if newTimePlayedThisMonth > values['allTimeHighPlayedPerMonth'] else values['allTimeHighPlayedPerMonth']

#   timesPlayedThisMonth
    newTimesPlayedThisMonth = values['timesPlayedThisMonth'] + 1 if lastUpdateToNowMonthsDiff == 0 else 1

#   avgTimesPlayedPerMonth
    newAvgTimesPlayedPerMonth = ((values['avgTimesPlayedThisMonth'] * (startToLastMonthsDiff + 1)) + 1) / (startToNowMonthsDiff + 1)

#   athTimesPlayedPerMonth
    newAthTimesPlayedPerMonth = newTimesPlayedThisMonth if newTimesPlayedThisMonth > values['athTimesPlayedPerMonth'] else values['athTimesPlayedPerMonth']

    return{
    'newTimePlayedThisMonth': secondsToString(newTimePlayedThisMonth),
    'newAvgTimePlayedPerMonth': secondsToString(int(newAvgTimePlayedPerMonth)),
    'newAthTimePerMonth': secondsToString(newAthTimePerMonth),
    'newTimesPlayedThisMonth': int(newTimesPlayedThisMonth),
    'newAvgTimesPlayedPerMonth': round(newAvgTimesPlayedPerMonth, 5),
    'newAthTimesPlayedPerMonth': int(newAthTimesPlayedPerMonth),
    }


def diff_Year(d1, d2):
    return (d1.year - d2.year)

def updateYears():
    startToLastYearsDiff = diff_Year(lastUpdatedObj, docCreatedObj)
    startToNowYearsDiff = diff_Year(currentDateObj, docCreatedObj)
    lastUpdateToNowYearsDiff = diff_Year(currentDateObj ,lastUpdatedObj)

#   timePlayedThisYear
    newTimePlayedThisYear = values['timePlayedThisYear'] + playTime if lastUpdateToNowYearsDiff == 0 else playTime

#   avgTimePlayedPerYear
    newAvgTimePlayedPerYear = (values['avgTimePlayedPerYear'] * (startToLastYearsDiff + 1) + playTime) / (startToNowYearsDiff + 1)

#   athTimePerYear
    newAthTimePerYear = newTimePlayedThisYear if newTimePlayedThisYear > values['allTimeHighPlayedPerYear'] else values['allTimeHighPlayedPerYear']

#   timesPlayedThisYear
    newTimesPlayedThisYear = values['timesPlayedThisYear'] + 1 if lastUpdateToNowYearsDiff == 0 else 1

#   avgTimesPlayedPerYear
    newAvgTimesPlayedPerYear = ((values['avgTimesPlayedThisYear'] * (startToLastYearsDiff + 1)) + 1) / (startToNowYearsDiff + 1)

#   athTimesPlayedPerYear
    newAthTimesPlayedPerYear = newTimesPlayedThisYear if newTimesPlayedThisYear > values['athTimesPlayedPerYear'] else values['athTimesPlayedPerYear']

    return{
    'newTimePlayedThisYear': secondsToString(newTimePlayedThisYear),
    'newAvgTimePlayedPerYear': secondsToString(int(newAvgTimePlayedPerYear)),
    'newAthTimePerYear': secondsToString(newAthTimePerYear),
    'newTimesPlayedThisYear': int(newTimesPlayedThisYear),
    'newAvgTimesPlayedPerYear': round(newAvgTimesPlayedPerYear, 5),
    'newAthTimesPlayedPerYear': int(newAthTimesPlayedPerYear),
    }

def updateRest():
    newTimePlayedAllTime = values['timePlayedAllTime'] + playTime
    newTimesPlayedTotal = values['timesPlayedTotal'] + 1
    # todo newAvgPlayTimePerSession is probably wrong!!  
    newAvgPlayTimePerSession = (values['avgplayTimePerSession'] * (newTimesPlayedTotal -1) + playTime) / newTimesPlayedTotal
    
    return{
    'newTimePlayedAllTime': secondsToString(newTimePlayedAllTime),
    'newTimesPlayedTotal': newTimesPlayedTotal,
    'newAvgPlayTimePerSession': secondsToString(int(newAvgPlayTimePerSession)),
    }

days = updateDays()
weeks = updateWeeks()
months = updateMonths()
years = updateYears()
rest = updateRest()
lastUpdatedString = str(currentDateObj.year) + '-' + str(currentDateObj.month) + '-' + str(currentDateObj.day)
docCreatedString = str(docCreatedObj.year) + '-' + str(docCreatedObj.month) + '-' + str(docCreatedObj.day)

filePath = "C:\\Users\Win 10 PC\Desktop\scripts\MxSim\mxStats\playTime.txt"
testFilePath = "C:\\Users\Win 10 PC\Desktop\scripts\MxSim\mxStats\output.txt"

# Write the file out again
with open(filePath, 'w') as file:
    file.write('**** Mx Simulator stats ****')
    file.write('\n\n')

    file.write('Times played total:               ' + str(rest['newTimesPlayedTotal']) + '\n')
    file.write('Time played all time:             ' + rest['newTimePlayedAllTime'] + '\n')
    file.write('Average play time per session:    ' + rest['newAvgPlayTimePerSession'] + '\n')
    file.write('\n')

    file.write('Time played this day:             ' + days['newTimePlayedThisDay'] + '\n') 
    file.write('Time played this week:            ' + weeks['newTimePlayedThisWeek'] + '\n')
    file.write('Time played this month:           ' + months['newTimePlayedThisMonth'] + '\n')
    file.write('Time played this year:            ' + years['newTimePlayedThisYear'] + '\n')
    file.write('\n')

    file.write('Average play time/day:            ' + days['newAvgTimePlayedPerDay'] + '\n')
    file.write('Average play time/week:           ' + weeks['newAvgTimePlayedPerWeek'] + '\n')
    file.write('Average play time/month:          ' + months['newAvgTimePlayedPerMonth'] + '\n')
    file.write('Average play time/year:           ' + years['newAvgTimePlayedPerYear'] + '\n')
    file.write('\n')

    file.write('All time high per day:            ' + days['newAthTimePerDay'] + '\n')
    file.write('All time high per week:           ' + weeks['newAthTimePerWeek'] + '\n')
    file.write('All time high per month:          ' + months['newAthTimePerMonth'] + '\n')
    file.write('All time high per year:           ' + years['newAthTimePerYear'] + '\n')

    file.write('\n')
    file.write('------------------------------------------')
    file.write('\n\n')

    file.write('Times played this day:            ' + str(days['newTimesPlayedThisDay']) + '\n')
    file.write('Times played this week:           ' + str(weeks['newTimesPlayedThisWeek']) + '\n')
    file.write('Times played this month:          ' + str(months['newTimesPlayedThisMonth']) + '\n')
    file.write('Times played this year:           ' + str(years['newTimesPlayedThisYear']) + '\n')
    file.write('\n')

    file.write('Average times played/day:         ' + str(days['newAvgTimesPlayedThisDay']) + '\n')
    file.write('Average times played/week:        ' + str(weeks['newAvgTimesPlayedPerWeek']) + '\n')
    file.write('Average times played/month:       ' + str(months['newAvgTimesPlayedPerMonth']) + '\n')
    file.write('Average times played/year:        ' + str(years['newAvgTimesPlayedPerYear']) + '\n')
    file.write('\n')

    file.write('All time high times played/day:   ' + str(days['newAthTimesPlayedPerDay']) + '\n')
    file.write('All time high times played/week:  ' + str(weeks['newAthTimesPlayedPerWeek']) + '\n')
    file.write('All time high times played/month: ' + str(months['newAthTimesPlayedPerMonth']) + '\n')
    file.write('All time high times played/year:  ' + str(years['newAthTimesPlayedPerYear']) + '\n')
    file.write('\n')

    file.write('doc last updated:                 ' + lastUpdatedString + '\n')
    file.write('doc created:                      ' + docCreatedString)













# create test case for all this crap
# assert diff_month(datetime(2010,10,1), datetime(2010,9,1)) == 1
# assert diff_month(datetime(2010,10,1), datetime(2009,10,1)) == 12
# assert diff_month(datetime(2010,10,1), datetime(2009,11,1)) == 11
# assert diff_month(datetime(2010,10,1), datetime(2009,8,1)) == 14


# sameDay sameWeek sameMonth sameYear       check
# !sameDay sameWeek sameMonth sameYear      check
# !sameDay !sameWeek sameMonth sameYear     
# !sameDay sameWeek !sameMonth sameYear
# !sameDay !sameWeek !sameMonth sameYear
# !sameDay !sameWeel !sameMonth !sameYear