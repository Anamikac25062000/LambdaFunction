#Create a Python module (a separate .py file) that contains a function to calculate the area of a rectangle. Then, in another Python script, import the module and use the function to calculate the area of a rectangle with specific dimensions. 

import area
length = 10
width = 2
area = area.calculate_area(length, width)
print(f"The area of a rectangle with length {length} and width {width} is: {area}")
