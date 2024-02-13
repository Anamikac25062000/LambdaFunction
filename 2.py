#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
 
def multiply(a):
    unknown_number = 10  
    return a * unknown_number

input_value = float(input("Enter a number: "))

result = multiply(input_value)

print(f"The result of multiplying {input_value} with an unknown number is: {result}")
