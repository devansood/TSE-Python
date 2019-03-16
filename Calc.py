#2.1
minutes = input("type minutes: ")
seconds = input("type seconds: ")
totals = (int(minutes)*60+int(seconds))
print(totals,"total seconds")
#2.2
print("how many KMs")
KMs = input()
totalmi = (int(KMs)*1.61)

print("You ran",totalmi,"miles")
#2.3
print("That's a total of",totals/60 / totalmi,"minutes per mile")
print("Your average was",totalmi / totals*3600,"miles per hour")
