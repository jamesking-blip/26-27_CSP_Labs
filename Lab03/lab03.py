
seconds = 10000
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds2 = seconds % 60
startingmilliseconds = 100000123
milliseconds = 10000123
seconds = milliseconds // 1000
milli_seconds_left = milliseconds % 1000
hours = seconds // 3600






print("starting milliseconds \t\t", startingmilliseconds)
print("Hours: \t\t" + str(hours))
print("Minutes: \t\t" + str(minutes))
print("Seconds: \t\t" + str(seconds2))
print("milliseconds: \t\t" + str(milliseconds))