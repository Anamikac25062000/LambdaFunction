#Write a Python program to find palindromes in a given list of strings using Lambda. 

palindrome = lambda a: a == a[::-1]

def find_palindromes(strings):
    return list(filter(palindrome, strings))

string_list = ["anamika", "level", "wow", "beinex"]

palindromes = find_palindromes(string_list)

print("List of palindromes:")
print(palindromes)
