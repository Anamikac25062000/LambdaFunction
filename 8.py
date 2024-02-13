#Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results. 
# Original list: [2, 4, 6, 9, 11] 
# Given number: 2 
# Result: 
# 4 8 12 18 22 

multiply_with_given_number = lambda x, factor: x * factor

original_list = [2, 4, 6, 9, 11]

given_number = 2

result_list = list(map(lambda x: multiply_with_given_number(x, given_number), original_list))

print("Original list:", original_list)
print("Given number:", given_number)
print("Result:")
print(" ".join(map(str, result_list)))
