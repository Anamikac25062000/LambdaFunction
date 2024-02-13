#Write a Python program to check whether a given string is a number or not using Lambda. 

is_number = lambda s: s.isdigit()

user_input = input("Enter a string to check if it's a number: ")

result = is_number(user_input)

if result:
    print(f"The input '{user_input}' is a number.")
else:
    print(f"The input '{user_input}' is not a number.")
