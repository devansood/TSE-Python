# import turtle
# leo = turtle.Turtle()
# # def square(t, length):
# #     for i in range(4):
# #         t.fd(length)
# #         t.lt(90)
# #
# # square(leo, 300)
# # print(square)
# # turtle.mainloop()
#
#
# import math
# #
# # def circle(t, r):
# #     circumference = 2 * math.pi * r
# #     n = 50
# #     length = circumference / n
# #     polygon(t, n, length)
# def polygon(t, n, length):
#     angle = 360.0 / n
#     polyline(t, n, length, angle)
#
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     polyline(t, n, step_length, step_angle)
#
# def polyline(t, n, length, angle):
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
#
# def circle(t, r):
#     arc(t, r, 360)
#
#
#
# print(circle)
# turtle.mainloop()
#
#
#
# def square_plus_one(a):
#     return a * a + 1
# square_plus_one(2)


# import cmath
# def quadratic(a, b, c):
#     d = b**2-4*a*c
#     d - (b (** 2) - (4 * a * c))
#     solution1 = (-b - cmath.sqrt(d)) / (2 * a)
#     solution2 = (-b + cmath.sqrt(d)) / (2 * a)
#
# quadratic(1, 2, 3)

#
#
# def quadratic1(a, b, c):
#     import math
#     sol_1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
#     sol_2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
#     return (sol_1, sol_2)
# print(quadratic1(1, 2,-3))


#
# def calcbmi():
#     ht = float(input("Enter Your Height"))
#     wt = float(input("Enter Your Weight"))
#     calcbmi = 703*(wt / ht**2)
#     if calcbmi <= 18.5:
#         print("Underweight")
#     elif calcbmi < 24.9:
#         print("normal weight")
#     elif calcbmi < 29.9:
#         print("overweight")
#     else:
#         print("very overweight")
#
# calcbmi()

# totalvalue = 0
# name = 'devan'
# for letter in name:
#     totalvalue = totalvalue + (ord(letter)-96)
# print(totalvalue)
#
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        import time
        time.sleep(1)
    print('blastoff!')

countdown(5)