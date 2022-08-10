number = input("insert a number: ")
number = int(number)
if number == 0:
    print("You inserted Zero: ", number)
elif number%2 == 0:
    print("Your inserted number is Even: ", number)
else:
    print("Your inserted number is Odd: ", number)