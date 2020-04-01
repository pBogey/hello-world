"""
04.01.2019 15:34
Alarm time
Bogdan Prădatu - exercise from how to think like a computer scientist
"""

from datetime import datetime

class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def print(time):
        """ return a time object in HH:MM:SS format """
        t = f"{time.hour:02d}:{time.minute:02d}:{time.second:02d}"
        return t

    def seconds(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self,seconds):
        self.second = seconds + self.second
        while self.second >= 60:
            self.second = self.second - 60
            self.minute = self.minute + 1
        while self.minute >= 60:
            self.minute = self.minute - 60
            self.hour = self.hour + 1
        while self.hour >= 24:
            self.hour = self.hour - 24

    def after(self,time2):
        if self.hour > time2.hour:
            return 1
        if self.hour < time2.hour:
            return 0
        if self.minute > time2.minute:
            return 1
        if self.minute < time2.minute:
            return 0
        if self.second > time2.second:
            return 1
        return 0



#currentTime = Time()
#currentTime.hours = 15
#currentTime.minutes = 34
#currentTime.seconds = 53

currentTime = datetime.now()

alarmTime = Time()
alarmTime.hour = 7
alarmTime.minute = 0
alarmTime.second = 0

alarmIn = Time()
alarmIn.hour = 8
alarmIn.minute = 30
alarmIn.second = 15

def convert_to_seconds(t):
    minutes = t.hour * 60 + t.minute
    seconds = minutes * 60 + t.second
    return seconds

def makeTime(seconds):
    time = Time()
    time.hour = seconds // 3600 - (24 * (seconds // 3600 // 24))
    time.minute = (seconds%3600) // 60
    time.second = seconds%60

    return time

def addTime(t1,t2):
    seconds = convert_to_seconds(t1)+convert_to_seconds(t2)
    return makeTime(seconds)

def time_left(currenttime,alarmtime):
    if currenttime.hour <= alarmtime.hour:
        seconds = (convert_to_seconds(alarmtime)
                   -convert_to_seconds(currenttime))
    else:
        seconds = (24*3600-convert_to_seconds(currenttime)
                   +convert_to_seconds(alarmtime))
    return makeTime(seconds)

def printTime(time):
    """ return a time object in HH:MM:SS format """
    time = f"{time.hour:02d}:{time.minute:02d}:{time.second:02d}"
    return time

print("Current Time:",printTime(currentTime))
print("**********")
print("Alarm set to go off at:",printTime(alarmTime))
print("""The alarm will go off in {0:02d} hours, {1:02d} minutes and {2:02d} seconds"""
      .format(time_left(currentTime,alarmTime).hour,
              time_left(currentTime,alarmTime).minute,
              time_left(currentTime,alarmTime).second))
print("**********")
#print("Alarm set to go off in:",printTime(alarmIn))     #function
print("Alarm set to go off in:",alarmIn.print())    #method
print("The alarm will go off at:",printTime(addTime(currentTime,alarmIn)))
