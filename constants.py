import tkinter as tk# import tkinter
import calendar
import datetime
import random
import string
import ast
import os

root = tk.Tk() # create a window
root.title("Planner")
root.geometry("900x750") # set the window size
root.configure(bg="#333333")
entry = tk.Entry(root)
#color controles
buttonGrey = '#444444'
lableGrey = '#333333'
dataBoxbg = lableGrey

lightBlue = '#B0C4DE'
green = '#66CD00'
pink = '#EE1289'

#tkinter functions
def forget_all(parent):
    for widget in parent.winfo_children():
        widget.forget()
#End tkinter
def rcButton(name, func):
    return tk.Button(
        root,
        text=name,
        command=func,
        fg=buttonbg, bg=buttonlc,
        height=3, width=8,
        font=("Arial", 12, "bold")
        ).pack()

def makeButton(name, func):
    return tk.Button(
        root,
        text=name,
        command=func,
        fg=buttonlc, bg=buttonbg,
        height=3, width=8,
        font=("Arial", 12, "bold")
        ).pack()

def sort_dates(dictLst):
    tempLst = dictLst.copy()
    return sorted(sorted(sorted(sorted(sorted(tempLst,
        key=lambda n: n['Time'][5]),
        key=lambda t: t['Time']),
        key=lambda d: d['Day']),
        key=lambda m: m['Month']),
        key=lambda y: y['Year']) 

def inTomorrow(dictLst, date):
    tempLst = []
    thisYear = date[0:4]#date
    thisMonth = date[5:7]
    thisDay = date[8:10]
    numThisDay = int(thisDay)
    if int(thisDay) + 1 > getDays(now):
        overDay = '0' + str((int(thisDay) + 1) - getDays(now))
        overMonth = str(int(thisMonth) + 1)
        overYear = thisYear
        if int(overMonth) > 12:
            overMonth = '01'
            overYear = str(int(thisYear) + 1)
        for diction in dictLst:
            print(f"dict: {int(diction['Year'] + diction['Month'] + diction['Day'])}, over: {int(overYear + overMonth + overDay)}")
            if int(diction['Year'] + diction['Month'] + diction['Day']) <= int(overYear + overMonth + overDay):
                if diction not in inToday(dictLst, date):
                    tempLst.append(diction)
    else:
        for diction in dictLst:
            if (diction['Year'] == thisYear) & (diction['Month'] == thisMonth) & (numThisDay + 1 == int(diction['Day'])):
                tempLst.append(diction)
    return tempLst

def inToday(dictLst, date):
    tempLst = []
    thisYear = date[0:4]#date
    thisMonth = date[5:7]
    thisDay = date[8:10]
    for diction in dictLst:
        if (diction['Year'] == thisYear) & (diction['Month'] == thisMonth) & (thisDay == diction['Day']):
            tempLst.append(diction)
    return tempLst

def timeOnly(today):
    time = today[11:13] + today[14:16]
    return time

def removeOld(dictLst, date, time):
    tempLst = []
    todayDate = int(date[0:4] + date[5:7] + date[8:10] + time)
    for diction in dictLst:
        eventDate = int(diction['Year'] + diction['Month'] + diction['Day'] + diction['Time'][0:2] + diction['Time'][3:5])
        if (int(diction['Time'][0:2]) < 12) & (diction['Time'][5] == 'p'):#if for example 01:30pm
            milTime = int(diction['Time'][0:2]) + 12 
            eventDate = int(diction['Year'] + diction['Month'] + diction['Day'] + str(milTime) + diction['Time'][3:5])
        if (int(diction['Time'][0:2]) == 12) & (diction['Time'][5] == 'a'):#if for example 12:30am
            eventDate = int(diction['Year'] + diction['Month'] + diction['Day'] + "00" + diction['Time'][3:5])
        if todayDate <= eventDate:
            tempLst.append(diction)
    return tempLst

def getDaysLeft(days, day):
    return days - int(day)

def dateOnly(today):
    date = ""
    for i in range(0, 10):
        date += today[i]
    return date

def getDay(date):
    day = ""
    for i in range(0, len(date)):
        if i >= 8:
            day += date[i]
    return day

def miniCal(now):
    return calendar.TextCalendar().formatmonth(now.year, now.month, w=3, l=0)# string of calender

def getDays(now):
    return calendar.monthrange(now.year, now.month)[1]#representing [0][1], 0 is lowest in range and 1 is highest

def initMessage(now, date, daysLeft):
    year = date[:4]
    month = date[5:7]
    day = date[8:]
    string = ''
    string += "\nGreetings from the PLANNER!\n" 
    string += f"\nTodays date is: {month}-{day}-{year}\n"
    string += f"There are {daysLeft} days left in this month.\n"
    return string

def inWeek(dictLst, date):
    thisWeek = []
    thisYear = date[0:4]#date
    thisMonth = date[5:7]
    thisDay = date[8:10]
    numThisDay = int(thisDay)
    if int(thisDay) + 7 > getDays(now):
        overDay = '0' + str((int(thisDay) + 7) - getDays(now))
        overMonth = str(int(thisMonth) + 1)
        overYear = thisYear
        if int(overMonth) > 12:
            overMonth = '01'
            overYear = str(int(thisYear) + 1)
        for diction in dictLst:
            #print(f"dict: {int(diction['Year'] + diction['Month'] + diction['Day'])}, over: {int(overYear + overMonth + overDay)}")
            if int(diction['Year'] + diction['Month'] + diction['Day']) <= int(overYear + overMonth + overDay):
                if (diction not in inToday(dictLst, date)) & (diction not in inTomorrow(dictLst, date)):
                    thisWeek.append(diction)
    else:
        for diction in dictLst:
            if (diction['Year'] == thisYear) & (diction['Month'] == thisMonth) & (numThisDay + 7 >= int(diction['Day'])):
                if (diction not in inToday(dictLst, date)) & (diction not in inTomorrow(dictLst, date)):
                    thisWeek.append(diction)
    return thisWeek

def randomStr(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def getLst(file):
    dictLst = []
    with open(file) as f: 
        data = f.read()
    dictLst = ast.literal_eval(data)
    return dictLst

def makeDict(event, year, month, day, time, apm, code):
    newDict = {}
    newDict.update({
        'Event': event,
        'Year': year,
        'Month': month,
        'Day': day,
        'Dayname': calendar.day_abbr[datetime.date(int(year), int(month), int(day)).weekday()],
        'Time': time[:2]+':'+time[2:]+apm,
        'Code': code
        })
    return newDict

def updateFile(Lst, file):
    with open(file, "w") as f:
        f.write(str(Lst))

def makeLable(string, size):
    return tk.Label(root, text=string, fg=lablelc, bg=lablebg, font=("Arial", size, "bold")).pack()

def newEntry():
    return tk.Entry(root, width=15, bg="#E3E3E3", borderwidth=5)

#entrys bg color change on focus
def on_focus_in(event):
    event.widget.config(bg=userColors[0])

def on_focus_out(event):
    event.widget.config(bg='white')

def on_return_next(event):
    event.widget.tk_focusNext().focus()

def entrys_focus_color(root):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.bind("<FocusIn>", on_focus_in)
            widget.bind("<FocusOut>", on_focus_out)
            widget.bind("<Return>", on_return_next)

colorsFile = 'pldata/colors.txt'
userColors = getLst(colorsFile)
buttonbg = buttonGrey
buttonlc = userColors[0]
lablebg = lableGrey
lablelc = userColors[0]
font_style = ("Helvetica", 12, "bold")
#globals
dataFile = "pldata/plannerData.txt"
now = datetime.datetime.now()
days = getDays(now)
today = str(datetime.datetime.today())
time = timeOnly(today)
date = dateOnly(today)
day = getDay(date)
daysLeft = getDaysLeft(days, day)
updateFile(removeOld(getLst(dataFile), date, time), dataFile)
dataLst = getLst(dataFile)