from time import process_time_ns

choice = input("Enter arithmetic operation: + - * / ")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
if choice == "+":
    print("Sum of number is", number1 + number2)
elif  choice == "-":
    print(f"sub of number is {number1 - number2}")
elif choice == "*":
    print(f"multiplication of number is {number1 * number2}")
elif choice == "/":
    print(f"division of number is {number1 / number2}")
else:
    print("your chociee is smoething else")

    """
    THE SMART COFFEE MACHINE PROBLEM

    This program uses nested 'if' statements to determine 
    a user's beverage order based on two choices:
    1. Drink type (Coffee or Tea)
    2. if he asks for Coffee : Milk preference (Yes or No)
    3. If he asks for tea : Sugar preference (Yes or No)
    """

    order = input("Enter order: Coffe or Tea :")
    if order == "Coffe" or order == "c":
        # print("Coffe")
        preference = input("you selected Coffee \n Do you want milk : Yes or No : ")
        if preference == "Yes" or preference == "y":
            print("Milk Added")
        else:
            print("Milk isn't Added")
    elif order == "Tea" or order == "t":
        print("Tea")
        preference = input("Do you want sugar : Yes or No : ")
        if preference == "Yes" or preference == "y":
            print("Sugar Added")
        else:
            print("Sugar isn't Added")
    else:
        print("Please enter Coffe or Tea ")