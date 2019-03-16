#Exercise 1
#1.1
import math
math.pi
math.pow
radius = float(input('Enter Radius: '))
volume = (4 / 3) * math.pi * (float(math.pow(radius, 3)))
print(round(volume, 2))

#1.2
copies = float(input("Number of Books Are You Ordering: "))
CPOB = round(((24.95 * .6) + 3) + ((24.96 * .6) + .75 * (copies - 1)),2)
print("$",CPOB,"Cost Total")

#1.3
start = (6*60+52)*60
easy = (8*60+15)*2
fast = (7*60+12)*3
finish_hour = (start + easy + fast)/(60*60.0)
finish_floored = (start + easy + fast)//(60*60)
finish_minute  = (finish_hour - finish_floored)*60
print('Finish time was %d:%d' % (finish_hour,finish_minute))

#1.4
grade = ((89 / 82) - 1)
print("Your Grade Went Up",round(grade, 2),"%")


