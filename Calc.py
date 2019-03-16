# print('minutes in 42 mins and 42 seconds:')
# print("42 * 60 + 42")
#
# print(40 * 60 + 42)
minutes = input("type minutes: ")
seconds = input("type seconds: ")
totals = (int(minutes)*60+int(seconds))
print(totals,"total seconds")

print("how many KMs")
KMs = input()
totalmi = (int(KMs)*1.61)

print("You ran",totalmi,"miles")

print("That's a total of",totals/60 / totalmi,"minutes per mile")
print("Your average was",totalmi / totals*3600,"miles per hour")
