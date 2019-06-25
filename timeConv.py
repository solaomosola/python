#f an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# find a total of all minutes
# find a number of hours hidden in minutes and update the hour
# correct minutes to fall in the (0..59) range
# correct hours to fall in the (0..23) range


hour = ((hour + ((mins+dura) // 60)) % 24)
mins = ((mins+dura) % 60)




print(hour, ":", mins, sep='')
