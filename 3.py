#Write a Python program to find if a given string starts with a given character using Lambda. 

start = lambda string, char: string.startswith(char)

string = input("Enter a string: ")
char = input("Enter a character to check if the string starts with it: ")

result = start(string, char)

if result:
    print(f"The string '{string}' starts with the character '{char}'.")
else:
    print(f"The string '{string}' does not start with the character '{char}'.")
