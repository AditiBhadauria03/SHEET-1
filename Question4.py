#4. WAP to check if the number is divisible by 7 or if the last digit is 5.

Num = int(input("Enter a number:"))
if Num % 7 == 0 and Num % 10 == 5:
    print("Number is divisible by 7 and the last digit is 5")
else:
    print("Number is not divisible by 7 and the last digit is not 5")