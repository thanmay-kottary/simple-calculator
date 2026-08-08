def add(x, y):
    #Return the sum of x and y.
    return x + y

def subtract(x, y):
    #Return the difference of x and y.
    return x - y

def multiply(x, y):
    #Return the product of x and y. 
    return x * y

def divide(x, y):
     #Return the quotient of x and y.
    if y == 0:
        return None
    return x / y

def percent(x, y):
    #Return the percentage of x and y.
    return (x / y) * 100

def square_root(x):
    #Return the square root of x.
    if x < 0:
        return None
    return x ** 0.5

def power(x, y):
    #Return x raised to the power of y.
    return x ** y


i=True
print("Welcome to the calculator program!")          
while i ==True:
    print("Select operation to perform:" )
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Square Root")
    print("7. Power")
    print("8. Exit")



    input_choice = int(input("Enter choice : "))
    if input_choice in (1, 2, 3, 4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if input_choice == 1:
            print("The sum is:" ,add(num1, num2))

        elif input_choice == 2:
            print("The difference is:" ,subtract(num1, num2))

        elif input_choice == 3:
            print("The product is:" ,multiply(num1, num2))

        elif input_choice == 4:
            if num1 == 0 and num2 == 0:
                print("Both numerator and denominator cannot be zero. The result is interminate because any number multiplied by zero fits the equation.")
            elif num2 == 0:
                print("Denominator cannot be zero. The result is undefined. No answer exists because any number multiplied by zero is always zero")
            else:
                print("The quotient is:" ,divide(num1, num2))

    elif input_choice == 5:
        num1 = float(input("Enter the part value: "))
        num2 = float(input("Enter the whole value: "))
        if num2 == 0:
            print("The whole value cannot be zero. The result is undefined because any number divided by zero is undefined.")
        else:
            print("The percentage is:" ,str(percent(num1, num2)) + "%")

    elif input_choice == 6:
        num1 = float(input("Enter the number to find the square root: "))
        if num1 < 0:
            print("Cannot compute the square root of a negative number. The result is undefined in the real number system.")
        else:
            print("The square root is:" ,square_root(num1))

    elif input_choice == 7:
        num1 = float(input("Enter the base number: "))
        num2 = float(input("Enter the exponent number: "))
        print("The result is:" ,power(num1, num2))

    elif input_choice == 8:
        print("Exiting the calculator. Goodbye!")
        exit()
  
    else:
        print("Invalid choice, Please select a valid operation from the menu.Try again.")
        i=True

    a=input("Do you want to perform another calculation? (yes/no): " )
    if a.lower() == "no":
        print("Exiting the calculator. Goodbye!")
        exit()
    elif a.lower() == "yes":
        i=True
