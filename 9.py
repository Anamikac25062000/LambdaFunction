#Write a Python program to find the maximum value in a given heterogeneous list using lambda.Original list: 
# ['Python', 3, 2, 4, 5, 'version'] 
# Maximum values in the said list using lambda:5 

original_list = ['Python', 3, 2, 4, 5, 'version']

find_max_value = lambda lst: max(filter(lambda x: isinstance(x, int), lst))

max_value = find_max_value(original_list)

print("Original list:", original_list)
print("Maximum value in the list using lambda:", max_value)
