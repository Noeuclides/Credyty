"""
python script to get the number of months that strat in a sundays in the XXth century
"""
year = [31, 28, 31, 30, 31, 30, 31, 31, 30,31,30,31]
yearBi = [31, 29, 31, 30, 31, 30, 31, 31, 30,31,30,31]
week = {1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat', 7:'Sun'}

first = 1
newday = first
sundays = 0
for month in year[:12]:
    newday = month % 7 + first
    if newday > 7:
        newday = newday % 7
    first = newday

for yearsincentury in range(1901, 2001):
    if yearsincentury % 4 == 0:
        oneyear = yearBi
    else:
        oneyear = year
    for month in oneyear: 
        newday = month % 7 + first
        if newday > 7:
            newday = newday % 7
        first = newday
        if first == 7:
            sundays += 1
print("The number of months that start in sunday in the XXth century are:", sundays)