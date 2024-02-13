#Write a Python program to check whether a given string is a number or not using Lambda. 

number = lambda s: s.isdigit()

input_value = input("Enter a string to check if it's a number: ")

result = number(input_value)

if result:
    print(f"The input '{input_value}' is a number.")
else:
    print(f"The input '{input_value}' is not a number.")
