#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result. 

add = lambda x: x + 15
multiplication = lambda x, y: print(x * y)
num = float(input("Enter a number: "))
print(add(num))
number1 = float(input("Enter the first number for multiplication: "))
number2 = float(input("Enter the second number for multiplication: "))
multiplication(number1, number2)
