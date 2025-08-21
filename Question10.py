#10. WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc.

A = int(input("Enter the number (1-7): "))

if A == 1:
    print("Monday")
elif A == 2:
    print("Tuesday")
elif A == 3:
    print("Wednesday")
elif A == 4:
    print("Thursday")
elif A == 5:
    print("Friday")
elif A == 6:
    print("Saturday")
elif A == 7:
    print("Sunday")
else:
    print(" A is an invalid number: ")