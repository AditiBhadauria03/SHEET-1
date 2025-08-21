#12.You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 180.

A = int(input("Enter angle a "))
B = int(input("Enter angle b "))
C = int(input("Enter angle c "))

if A + B + C == 180 and A > 0 and B > 0 and C > 0:
    print("The Tringle is valid")
else:
    print("The Triangle is not valid")
