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

class App:
    def __init__(self):
        self.results = []
        self.newLst = []
        self.foundDict = {}
        self.entries = []
        self.count = 0
        self.count2 = 0
        self.func = None
        self.code = None
        self.dataLst = getLst(dataFile)
        self.weekEvents = inWeek(self.dataLst, date)
        self.dataFile = dataFile
        self.now = now
        self.days = days
        self.today = today
        self.thisTime = time
        self.date = date
        self.thisDay = day
        self.daysLeft = daysLeft
        self.schedual = '\n*New Event Manager*'

    def errMessage(self):
        self.count = 0
        forget_all(root)
        makeLable('\n\n\n-Error0: Incorrect Format\n', 16)
        makeButton('Home', self.btm)
        makeButton('Try Again', self.newEvent)
        makeButton('Options', self.options)
        root.mainloop()

    def errMessage1(self):
        self.count = 0
        forget_all(root)
        makeLable('\n\n\n-Error0: Input Error\n', 16)
        makeButton('Home', self.btm)
        makeButton('Try Again', self.newEvent)
        makeButton('Options', self.options)
        root.mainloop()

    def errorMessage3(self):
        self.count = 0
        forget_all(root)
        makeLable(f'\n\n\n-Error3: {self.results[0]} Not In Data..\n\n', 16)
        makeButton('Home', self.btm)
        makeButton('Try Again', self.editData)
        makeButton('Options', self.options)
        root.mainloop()

    def errorMessage4(self):
        self.count = 0
        forget_all(root)
        makeLable(f'\n\n\n-Error4: {self.results[0]} Not In Data..\n\n', 16)
        makeButton('Home', self.btm)
        makeButton('Try Again', self.unschedual)
        makeButton('Options', self.options)
        root.mainloop()

    def ohno(self):
        forget_all(root)
        makeLable('\n\n\n-Exception raised:\nThe Date You Entered Dosent Exist.\n', 16)
        makeButton('Try Again', self.newEvent)
        makeButton('Home', self.btm)
        makeButton('Options', self.options)

    def submitNew(self):
        newLst = []
        eventDict = {}
        try:
            if self.code == None:
                self.code = randomStr(4)
            if (len(self.results) == 6):
                usrData = Answers(self.results[0], self.results[1], self.results[2], self.results[3], self.results[4], self.results[5])
                #self.debuger(usrData.check())
                if usrData.check() == {True}:
                    eventDict = makeDict(self.results[0], self.results[1], self.results[2], self.results[3], self.results[4], self.results[5], self.code)
                    newLst.append(eventDict)
                    for item in self.dataLst:
                        if self.code != item['Code']: #a bug exist, theres a small chance the random code is generated twice
                            newLst.append(item)
                    updateFile(newLst, self.dataFile)
                else:
                    self.errMessage()
            else:
                self.errMessage1()
            self.btm()
        except Exception as _:
            self.ohno()

    def dataStr2(self, subject, dictLst):
        tempLst = sort_dates(dictLst)
        string = ''
        if tempLst == []:
            makeLable(f'No Events {subject}..', 18)
            return ''
        else:
            makeLable(f'Events {subject}!\n', 18)
            for data in tempLst:
                string += f"{data['Event']} on {data['Dayname']} {data['Month']}-{data['Day']}-{data['Year']} at {data['Time']}. ID#{data['Code']}\n" 
        return string

    def debuger(self, value):
        print(f'DEBUGGER::{value}::')

    def btm(self):
        forget_all(root)
        main()

    def newEvent(self):
        self.count = 0
        self.count2 = 6
        self.results = []
        self.entries = []
        self.func = self.submitNew
        forget_all(root)
        event,year ,month ,day , time, apm = 0, 0, 0, 0, 0, 0
        makeLable('\n*Edit Event Manager*\n', 18)
        makeLable(f'What Event?', 12)
        event = tk.Entry(root)
        event.pack()
        event.focus_set()
        makeLable(f'\nWhat Year?\nxxxx', 12)
        year = tk.Entry(root)
        year.pack()
        makeLable(f'\nWhat Month?\nxx', 12)
        month = tk.Entry(root)
        month.pack()
        makeLable(f'\nWhat day?\nxx', 12)
        day = tk.Entry(root)
        day.pack()
        makeLable(f'\nWhat time?\nxxxx', 12)
        time = tk.Entry(root)
        time.pack()
        makeLable(f'\nam or pm?', 12)
        apm = tk.Entry(root)
        apm.pack()
        entrys_focus_color(root)
        def assighn():
            self.results = [event.get(), year.get(), month.get(), day.get(), time.get(), apm.get()]
            self.func()
        makeButton('Submit', assighn)
        makeButton('Home', self.btm)
        makeButton('Options', self.options)
        root.mainloop()

    def changeData(self):
        event,year ,month ,day , time, apm = 0, 0, 0, 0, 0, 0
        self.count = 0
        self.count2 = 6
        self.entries = []
        self.func = self.submitNew
        if self.results[0] not in map(lambda d: d.get('Code'), self.dataLst):
            self.errorMessage3()
        forget_all(root)
        self.code = self.results[0]
        self.results = []
        makeLable('\n*Edit Event Manager*\n', 18)
        makeLable(f'What Event?', 12)
        event = tk.Entry(root)
        event.pack()
        event.focus_set()
        makeLable(f'\nWhat Year?\nxxxx', 12)
        year = tk.Entry(root)
        year.pack()
        makeLable(f'\nWhat Month?\nxx', 12)
        month = tk.Entry(root)
        month.pack()
        makeLable(f'\nWhat day?\nxx', 12)
        day = tk.Entry(root)
        day.pack()
        makeLable(f'\nWhat time?\nxxxx', 12)
        time = tk.Entry(root)
        time.pack()
        makeLable(f'\nam or pm?', 12)
        apm = tk.Entry(root)
        apm.pack()
        entrys_focus_color(root)
        def assighn():
            self.results = [event.get(), year.get(), month.get(), day.get(), time.get(), apm.get()]
            self.func()
        makeButton('Submit', assighn)
        makeButton('Home', self.btm)
        makeButton('Options', self.options)
        root.mainloop()


    def editData(self):
        self.count = 0
        self.count2 = 1
        self.results = []
        self.entries = []
        self.func = self.changeData
        code = ''
        forget_all(root)
        makeLable('\n*Enter In Event Manager*\n\n', 18)
        self.dataBox2('Stored', self.dataLst)
        makeLable(f'\nEnter ID#', 12)
        id = tk.Entry(root)
        id.pack()
        id.focus_set()
        entrys_focus_color(root)
        def assighn():
            self.results = [id.get()]
            self.func()
        makeButton('Submit', assighn)
        makeButton('Home', self.btm)
        makeButton('Options', self.options)

    def removeData(self):
        self.code = self.results[0]
        newLst = []
        if self.code not in map(lambda d: d.get('Code'), self.dataLst):
            self.errorMessage4()
        self.dataBox2('Stored', self.dataLst)
        for diction in self.dataLst:
            if diction['Code'] != self.code:
                newLst.append(diction)
            else:
                self.foundDict = diction
        self.areYouShure()

    def areYouShure(self):
        forget_all(root)
        self.entries = []
        event = self.foundDict['Event']
        dayname = self.foundDict['Dayname']
        year = self.foundDict['Year']
        month = self.foundDict['Month']
        day = self.foundDict['Day']
        time = self.foundDict['Time']
        self.code = self.foundDict['Code']
        makeLable('\n*Delete Event Manager*\n\n', 18)
        makeLable(f"\nAre You Sure You Want To Delete This?", 16)
        makeLable(f"\n{event} on {dayname} {month}-{day}-{year} at {time}\n", 16)
        makeButton('Yes', self.removeCode)
        makeButton('No - Home', self.btm)
        makeButton('Try Again', self.unschedual)
        makeButton('Options', self.options)
        root.mainloop()

    def removeCode(self):
        newLst = []
        for item in self.dataLst:
            if self.code != item['Code']:
                newLst.append(item)
            updateFile(newLst, self.dataFile)
        self.btm() 

    def unschedual(self):
        self.count = 0
        self.count2 = 1
        self.results = []
        self.entries = []
        self.func = self.removeData
        code = ''
        forget_all(root)
        makeLable('\n*Delete Event Manager*\n\n', 18)
        self.dataBox2('Stored', self.dataLst)
        id = tk.Entry(root)
        id.pack()
        id.focus_set()
        entrys_focus_color(root)
        def assighn():
            self.results = [id.get()]
            self.func()
        makeButton('Submit', assighn)
        makeButton('Home', self.btm)
        makeButton('Options', self.options)
        root.mainloop()

    def dataBox2(self, subject, dictLst):
        return tk.Label(root, text=self.dataStr2(subject, dictLst), bg=dataBoxbg, fg=lablelc, font=("Arial", 16, "bold"), padx=10, pady=5).pack()

    def checkSchedual(self):
        forget_all(root)
        makeLable('\n\n\n\n', 12)
        self.dataBox2('Scheduled', self.dataLst)
        makeButton('Home', self.btm)
        makeButton('Options', self.options)
        root.mainloop()

    def checkWeek(self):
        forget_all(root)
        makeLable('\n\n\n\n', 12)
        self.dataBox2('This Week', inWeek(self.dataLst, date))
        makeButton('Home', self.btm)
        makeButton('Options', self.options)
        root.mainloop()

    def checkTomorrow(self):
        forget_all(root)
        makeLable('\n\n\n\n', 12)
        self.dataBox2('Tomorrow', inTomorrow(self.dataLst, date))
        makeButton('Home', self.btm)
        makeButton('Options', self.options)
        root.mainloop()

    def checkToday(self):
        forget_all(root)
        makeLable('\n\n\n\n', 12)
        self.dataBox2('Today', inToday(self.dataLst, date))
        makeButton('Home', self.btm)
        makeButton('Options', self.options)

    def options(self):
        forget_all(root)
        makeLable(initMessage(now, date, daysLeft), 18)
        tk.Label(root, text=miniCal(now), font="TkFixedFont", justify=tk.LEFT, fg=lablelc, bg=lablebg).pack()
        makeButton('Schedule', self.newEvent)
        makeButton('Remove', self.unschedual)
        makeButton('Edit', self.editData)
        makeButton('Home', self.btm)
        tk.Button(
        root,
        text='Settings',
        command=self.settings,
        fg=buttonlc, bg=buttonbg,
        height=1, width=8,
        font=("Arial", 12, "bold")
        ).pack()
        root.mainloop()

    def scheme2(self):
        global buttonlc
        global lablelc
        global userColors
        buttonlc = green
        lablelc = green
        userColors[0] = green
        updateFile(userColors, colorsFile)
        self.settings()
        
    def scheme1(self):
        global buttonlc
        global lablelc
        global userColors
        buttonlc = lightBlue
        lablelc = lightBlue
        userColors[0] = lightBlue
        updateFile(userColors, colorsFile)
        self.settings()

    def scheme3(self):
        global buttonlc
        global lablelc
        global userColors
        buttonlc = pink
        lablelc = pink
        userColors[0] = pink
        updateFile(userColors, colorsFile)
        self.settings()

    def settings(self):
        forget_all(root)
        makeLable('\n*Settings Manager*\n\n', 18)
        makeButton('Scheme 1', self.scheme1)
        makeButton('Scheme 2', self.scheme2)
        makeButton('Scheme 3', self.scheme3)
        makeButton('Home', self.btm)
        root.mainloop()

class Answers:
    def __init__(self, event, year, month, day, time, apm):
        self.event = str(event),
        self.year = str(year),
        self.month = str(month),
        self.day = str(day),
        self.time = str(time),
        self.apm = str(apm)

    def printAnswers(self):
        return print(str(self.event[0]) + str(self.year[0]) + str(self.month[0]) + str(self.day[0]) + str(self.time[0]) + str(self.apm))

    def check(self):
        check1 = (len(self.year[0]) == 4) & (all(map(lambda c: c.isdigit(), str(self.year[0]))))
        check2 = ((len(self.month[0]) == 2) & (all(map(lambda c: c.isdigit(), str(self.month[0])))) & (int(self.month[0]) <= 12))
        check3 = ((len(self.day[0]) == 2) & (all(map(lambda c: c.isdigit(), str(self.day[0])))))
        check4 = ((len(self.time[0]) == 4) & (all(map(lambda c: c.isdigit(), str(self.time[0])))))
        check5 = ((self.apm == 'am') | (self.apm == 'pm'))
        check6 = ((int(self.time[0][:2]) <= 12) & (int(self.time[0][2:]) <= 59))
        #self.printAnswers()
        return {check1, check2, check3, check4, check5, check6}

def main():
    user = App()
    updateFile(removeOld(getLst(dataFile), date, time), dataFile)
    #print initmessage
    makeLable(initMessage(now, date, daysLeft), 18)
    #pint calendar
    tk.Label(root, text=miniCal(now), font="TkFixedFont", justify=tk.LEFT, fg=lablelc, bg=lablebg).pack()
    rcButton('Today\n'+str(len(inToday(getLst(dataFile), date))), user.checkToday)
    rcButton('Tomorrow\n'+str(len(inTomorrow(getLst(dataFile), date))), user.checkTomorrow)
    rcButton('This Week\n'+str(len(inWeek(getLst(dataFile), date))), user.checkWeek)
    rcButton('All Data\n'+str(len(getLst(dataFile))), user.checkSchedual)
    makeButton('Options', user.options)
    tk.Label(root, text='\n\n\nDeveloped By Thomas Gomez @https://github.com/BruzaTom', fg=lablelc, bg="#333333", font=("Arial", 10, "bold")).pack()
    root.mainloop()
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
    event.widget.config(bg='lightblue')

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

main()
