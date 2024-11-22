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