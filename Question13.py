#13. Write a program to input two numbers(A & B) from the user and print the maximu element among A & B.

A = int(input("Enter the number"))
B = int(input("Enter the number"))

if A > B :
    print(" A is maximum element")
elif B > A :
    print(" B is maximum element")
else:
    print("Both are equal")