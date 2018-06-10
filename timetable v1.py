import random # to select subjects
#import sys    # to exit the program

subjects = [] # sets up subjects list
while True:
    print("Enter subject number " + str(len(subjects)+1) + ", or press return to finish.")
    subjectName = input()
    if subjectName == "":
        break
    subjects = subjects + [subjectName] # adds input to subjects list, loops back to the start

print("Your subjects are:")
for subjectName in subjects:
    print("  " + subjectName)

monday = [] # sets up a list (which will contain subjects) for each day
tuesday = []
wednesday = []
thursday = []
friday = []

week = [monday, tuesday, wednesday, thursday, friday]

def timetable(day):
    while len(day) < 2:
    #try:
        if len(subjects) == 0:
    # for i in range(len(week)):
    #  subjects.append(week[i])
            for dayOfWeek in range(len(week)):
                for thingInDay in range(len(week[dayOfWeek])):
                    subjects.append(week[dayOfWeek][thingInDay])
            
        choice = random.choice(subjects)
        day.append(choice)
        subjects.remove(choice)
    print("DAY " + str((week.index(day))+1))
    print("I have timetabled " + str(day))
    #print("Your remaining subjects are " + str(subjects))
    print("")    
    #except IndexError:
    #subjects.append(week)
    #print(subjects)
            
for i in range(len(week)):       
        #print("DAY " + str(((i)+1)))
        timetable(week[i])
        

#while True:
    #print("Enter the day you would like timetabling, or press return to finish.")
    #currentDay = input()
    #if currentDay in week:
    #timetable(currentDay)
    #if currentDay == "":
      #  sys.exit()
    #else:
        #print("You must enter one of " + str(week))
        




