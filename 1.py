#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result. 

add_15 = lambda x: x + 15
multiplication = lambda x, y: print(x * y)
number = float(input("Enter a number: "))
x_value = float(input("Enter the first number for multiplication: "))
x_value = float(input("Enter the second number for multiplication: "))
result_add_15 = add_15(number)
print(f"Adding 15 to {number} gives: {result_add_15}")

print(f"Multiplying {x_value} and {y_value} gives:", end=" ")
multiplication(x_value, y_value)
