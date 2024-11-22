import tkinter as tk# import tkinter
from constants import *
from answers import Answers

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
        updateFile(removeOld(getLst(dataFile), date, time), dataFile)
        #print initmessage
        makeLable(initMessage(now, date, daysLeft), 18)
        #pint calendar
        tk.Label(root, text=miniCal(now), font="TkFixedFont", justify=tk.LEFT, fg=lablelc, bg=lablebg).pack()
        rcButton('Today\n'+str(len(inToday(getLst(dataFile), date))), self.checkToday)
        rcButton('Tomorrow\n'+str(len(inTomorrow(getLst(dataFile), date))), self.checkTomorrow)
        rcButton('This Week\n'+str(len(inWeek(getLst(dataFile), date))), self.checkWeek)
        rcButton('All Data\n'+str(len(getLst(dataFile))), self.checkSchedual)
        makeButton('Options', self.options)
        tk.Label(root, text='\n\n\nDeveloped By Thomas Gomez @https://github.com/BruzaTom', fg=lablelc, bg="#333333", font=("Arial", 10, "bold")).pack()
        root.mainloop()

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
        event = tk.Entry(root, insertwidth=6, font=font_style)
        event.pack()
        event.focus_set()
        makeLable(f'\nWhat Year?\nxxxx', 12)
        year = tk.Entry(root, insertwidth=6, font=font_style)
        year.pack()
        makeLable(f'\nWhat Month?\nxx', 12)
        month = tk.Entry(root, insertwidth=6, font=font_style)
        month.pack()
        makeLable(f'\nWhat day?\nxx', 12)
        day = tk.Entry(root, insertwidth=6, font=font_style)
        day.pack()
        makeLable(f'\nWhat time?\nxxxx', 12)
        time = tk.Entry(root, insertwidth=6, font=font_style)
        time.pack()
        makeLable(f'\nam or pm?', 12)
        apm = tk.Entry(root, insertwidth=6, font=font_style)
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
        event = tk.Entry(root, insertwidth=6, font=font_style)
        event.pack()
        event.focus_set()
        makeLable(f'\nWhat Year?\nxxxx', 12)
        year = tk.Entry(root, insertwidth=6, font=font_style)
        year.pack()
        makeLable(f'\nWhat Month?\nxx', 12)
        month = tk.Entry(root, insertwidth=6, font=font_style)
        month.pack()
        makeLable(f'\nWhat day?\nxx', 12)
        day = tk.Entry(root, insertwidth=6, font=font_style)
        day.pack()
        makeLable(f'\nWhat time?\nxxxx', 12)
        time = tk.Entry(root, insertwidth=6, font=font_style)
        time.pack()
        makeLable(f'\nam or pm?', 12)
        apm = tk.Entry(root, insertwidth=6, font=font_style)
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
        id = tk.Entry(root, insertwidth=6, font=font_style)
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
        id = tk.Entry(root, insertwidth=6, font=font_style)
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