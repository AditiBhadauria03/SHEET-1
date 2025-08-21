#14. Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C.

A = int(input("Enter first number : "))
B = int(input("Enter second number : "))
C = int(input("Enter third number : "))

# Comparing numbers
if A <= B and A <= C:
    print("Minimum number is:", A)
elif B <= A and B <= C:
    print("Minimum number is:", B)
else:
    print("Minimum number is:", C)