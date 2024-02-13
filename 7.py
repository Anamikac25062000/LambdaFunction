#Write a Python program to find palindromes in a given list of strings using Lambda. 

is_palindrome = lambda s: s == s[::-1]

def find_palindromes(strings):
    return list(filter(is_palindrome, strings))

string_list = ["level", "python", "radar", "hello", "madam", "world"]

palindromes = find_palindromes(string_list)

print("List of palindromes:")
print(palindromes)
