#2.1
minutes = input("Number of minutes: ")
seconds = input("Number of seconds: ")
totals = (int(minutes)*60+int(seconds))
print(totals,"total seconds")
#2.2
print("how many KMs")
KMs = input()
totalmi = (int(KMs)*1.61)

print("You ran",totalmi,"miles")
#2.3
print("That's a total of",round(totals/60 / totalmi,3),"minutes per mile")
print("Your average was",round(totalmi / totals*3600,3),"miles per hour")
