import tkinter as tk# import tkinter
from constants import *
from app import App

def main():
    user = App()
    updateFile(removeOld(getLst(dataFile), date, time), dataFile)
    #print initmessage
    makelable(initMessage(now, date, daysLeft), 18)
    #pint calendar
    tk.Label(root, text=miniCal(now), font="TkFixedFont", justify=tk.LEFT, fg=lablelc, bg=lablebg).pack()
    rcButton('Today\n'+str(len(inToday(getLst(dataFile), date))), user.checkToday)
    rcButton('Tomorrow\n'+str(len(inTomorrow(getLst(dataFile), date))), user.checkTomorrow)
    rcButton('This Week\n'+str(len(inWeek(getLst(dataFile), date))), user.checkWeek)
    rcButton('All Data\n'+str(len(getLst(dataFile))), user.checkSchedual)
    makeButton('Options', user.options)
    tk.Label(root, text='\n\n\nDeveloped By Thomas Gomez @https://github.com/BruzaTom', fg=lablelc, bg="#333333", font=("Arial", 10, "bold")).pack()
    root.mainloop()


main()
