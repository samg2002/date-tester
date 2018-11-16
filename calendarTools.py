from math import *


##A dictionary for all the months
months = {"Jan" : 1,"Feb" : 2,"Mar" : 3,"Apr" : 4,"May" : 5,"Jun" : 6,"Jul" : 7,"Aug" : 8,"Sep" : 9,"Oct" : 10,"Nov" : 11,"Dec" : 12}

##An Array that stores the number of days in each month
monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]

def calculateDaysBetween(date0,date1):

    date0Array = date0.split(" ")
    date1Array = date1.split(" ")

    day0 = int(date0Array[1][:-1])
    day1 = int(date1Array[1][:-1])

    month0 = months[date0Array[0]]
    month1 = months[date1Array[0]]
    

    year0 = int(date0Array[2]) 
    year1 = int(date1Array[2])


    if year0 == year1:
        if month0 == month1:
            return abs (betweenDays (day0,day1))

        elif month0 != month1:
            return countDaysWithinYear(month0,day0,month1,day1,year0)

    else:
        if year0 > year1:
            smallerYear = year1
            biggerYear = year0
            smallerMonth = month1
            biggerMonth = month0
            smallerDay = day1
            biggerDay = day0

        else:
            smallerYear = year0
            biggerYear = year1
            smallerMonth = month0
            biggerMonth = month1
            smallerDay = day0
            biggerDay = day1
                    
        daysUntillEndOfYear = countDaysWithinYear(smallerMonth,smallerDay,12,31,smallerYear)
        daysFromStartOfYear = countDaysWithinYear(biggerMonth,biggerDay,1,1,biggerYear)
        
        daysOfYearsInBetween = 0

        for i in range(biggerYear-smallerYear-1):
            daysOfYearsInBetween = daysOfYearsInBetween + 365
            if isLeapYear(i + smallerYear + 1):
                daysOfYearsInBetween = daysOfYearsInBetween + 1

        return daysOfYearsInBetween + daysUntillEndOfYear + daysFromStartOfYear + 1
                
            
            
            


        
            

def getDaysInMonth(month,year):
    if month == 2:
        if isLeapYear(year):

            return 29
        
    return monthDays[month-1]
            
            

##A function that checks if a year is a Leap Year
def isLeapYear(year):
    return  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
            
            
            
                

   
#A function that finds the difference between days 
def betweenDays(day0,day1):

    difference = (day0-day1)

    return difference


##A function that calculates the difference between dates
def countDaysWithinYear(month0,day0,month1,day1,year):
    
    smallerMonth = 0 ##A variable that determines which of the months is the first in chronological order
    
    biggerMonth = 0 ##A variable that determines which of the months is last in chronological order
    
    daysTillMonthEnds = 0 ##A variable that calculates the amount of days left in the month from the first date
    
    daysIntoMonth = 0 ##A variable that calculates the amount of days into a month for later date
    
    if month0 > month1:
        smallerMonth = month1
        biggerMonth = month0
        daysTillMonthEnds = getDaysInMonth(month1,year)-day1
        daysIntoMonth = day0

    elif month1 > month0:
        smallerMonth = month0
        biggerMonth = month1
        daysTillMonthEnds = getDaysInMonth(month0,year)-day0
        daysIntoMonth = day1
    else:
        return abs(betweenDays(day1, day0))
            
    daysBetweenMonths = 0 ##A variable for calculating the amount of years/months/days between the two given dates
        
    for i in range(biggerMonth-smallerMonth-1):
        daysBetweenMonths = daysBetweenMonths + getDaysInMonth(smallerMonth + i + 1,year)

    return daysBetweenMonths + daysTillMonthEnds + daysIntoMonth



