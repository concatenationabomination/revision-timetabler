import random #to select subjects

subjects = []
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

week = [monday, tuesday, wednesday, thursday, friday] # sets up a MEGA LIST holding the other lists

def timetable(day):
    while len(day) < 2: # integer = number of subjects timetabled per day

        if len(subjects) == 0: # if all the subjects have been removed from pool, then...
            for dayOfWeek in range(len(week)): # for each day of the week...
                for thingInDay in range(len(week[dayOfWeek])): # ...that holds stuff...
                    subjects.append(week[dayOfWeek][thingInDay]) #... put stuff from those days back into to the subject pool
            
        choice = random.choice(subjects)
        day.append(choice)
        subjects.remove(choice) # take it 'out of the pool' until everything has been chosen - like a song shuffle

    print("DAY " + str((week.index(day))+1))
    print("I have timetabled " + str(day))
    #print("Your remaining subjects are " + str(subjects))
    print("")    
            
for i in range(len(week)): # for each day of the week, timetable stuff     
        timetable(week[i])
