M = 'Monday'
T = 'Tuesday'
W = 'Wednesday'
R = 'Thursday'
F = 'Friday'
S = 'Saturday'
U = 'Sunday'
def determineDay( dayMilestone, interval):
    daysInWeek = 7
    weekday2NumberDict = {
        M: 0,
        T: 1, 
        W: 2, 
        R: 3, 
        F: 4, 
        S: 5, 
        U: 6
    }
    number2WeekdayDict = {
        0: M,
        1: T,
        2: W,
        3: R,
        4: F,
        5: S,
        6: U
    }
    return number2WeekdayDict.get( (weekday2NumberDict.get(dayMilestone) + interval ) % daysInWeek)
def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
