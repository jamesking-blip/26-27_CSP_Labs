
seconds = 10000
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds2 = seconds % 60
startingmilliseconds = 100000123
milliseconds = startingmilliseconds % seconds


print(startingmilliseconds)
print(hours)
print(minutes)
print(seconds2)
print(milliseconds)