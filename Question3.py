#3. WAP to check if the number is divisible by 3 and the last digit is 4.

Num = int(input("Enter a number:"))
if Num % 3 == 0 and Num % 10 == 4:
    print("Number is divisible by 3 and the last digit is 4")
else:
    print("Number is not divisibe by 3 and the last digit is not 4")