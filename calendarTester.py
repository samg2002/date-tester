from calendarTools import *



dateZeros = ["Jan 01, 2018","Jan 09, 2018","Dec 31, 2018","Mar 05, 2015","Jul 20, 2002"]
dateOnes = ["Feb 01, 2018","Mar 21, 2018","Jan 03, 2019","Jan 01, 2018","Oct 22, 2008"]

for i in range(len(dateZeros)):
    print ("The amount of days between date1 and date2 is",calculateDaysBetween(dateZeros[i],dateOnes[i]),"days")
