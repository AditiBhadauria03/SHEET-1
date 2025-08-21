#7. Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle).

A = int(input("Enter the angle"))
B = int(input("Enter the angle"))
C = int(input("Enter the angle"))
if A + B + C == 180 and A > 0 and B > 0 and C > 0:
    if A == 90 or B == 90 or C == 90:
        print("Right Triangle")
    elif A > 90 or B > 90 or C > 90:
        print("Obtuse Trinagle")
    else:
        print("Acute Triangle")
else:
    print("Invalid angles")