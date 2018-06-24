# This program works like a song shuffle, with 2 pools of candidates.
# Subjects are randomly chosen from the active pool and added to the day in question.
# That subject is them removed from the active pool and added to the inactive pool.
# Once the active pool is empty it becomes the inactive pool (and vice versa).

import random # to select subjects

subjectPoolA = []
subjectPoolB = []

while True:
    print("Enter subject number " + str(len(subjectPoolA)+1) + ", or press return to finish.")
    subjectName = input()
    if subjectName == "":
        break
    subjectPoolA = subjectPoolA + [subjectName] # adds input to subjects list, loops back to the start

print("Your subjects are:")
for subjectName in subjectPoolA:
    print("  " + subjectName)

    
monday = [] # sets up a list (which will contain subjects) for each day
tuesday = []
wednesday = []
thursday = []
friday = []

week = [monday, tuesday, wednesday, thursday, friday] # sets up a MEGA LIST holding the other lists


def timetable(day):
    poolNumber = 1 # ugly ugly local variables
    activePool = subjectPoolA
    inactivePool = subjectPoolB
    
    while len(day) < 2: # integer = number of subjects timetabled per day 
        if len(activePool) == 0: # this all makes sure active pool != 0
                poolNumber += 1
                
                if poolNumber % 2 == 0: # even numbers = poolB 
                    activePool = subjectPoolB
                    inactivePool = subjectPoolA
                    
                else:
                    activePool = subjectPoolA # odd numbers = poolA - ie, active/inactive pools swap when empty
                    inactivePool = subjectPoolB                                     

        choice = random.choice(activePool) # timetable
        day.append(choice)
        activePool.remove(choice)
        inactivePool.append(choice)

    print("DAY " + str((week.index(day))+1))
    print("I have timetabled " + str(day) + "\n")  
        

for i in range(len(week)): # for each day of the week, timetable stuff     
        timetable(week[i])

