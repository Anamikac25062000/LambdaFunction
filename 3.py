#Write a Python program to find if a given string starts with a given character using Lambda. 

starts_with_char = lambda string, char: string.startswith(char)

user_string = input("Enter a string: ")
user_char = input("Enter a character to check if the string starts with it: ")

result = starts_with_char(user_string, user_char)

if result:
    print(f"The string '{user_string}' starts with the character '{user_char}'.")
else:
    print(f"The string '{user_string}' does not start with the character '{user_char}'.")
