#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
 
def multiply_with_unknown(x):
    unknown_number = 10  
    return x * unknown_number

user_input = float(input("Enter a number: "))

result = multiply_with_unknown(user_input)

print(f"The result of multiplying {user_input} with an unknown number is: {result}")
