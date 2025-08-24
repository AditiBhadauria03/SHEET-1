#6. Read three integers and print their maximum.

A = int(input("Enter first number : "))
B = int(input("Enter second number : "))
C = int(input("Enter third number : "))

if A >= B and A >= C:
    print("Maximum number is:", A)
elif B >= A and B >= C:
    print("Maximum number is:", B)
else:
    print("Maximum number is:", C)
