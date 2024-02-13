#Create a Python module (a separate .py file) that contains a function to calculate the area of a rectangle. Then, in another Python script, import the module and use the function to calculate the area of a rectangle with specific dimensions. 

import area
length = 5.0
width = 3.0
area = area.calculate_rectangle_area(length, width)
print(f"The area of a rectangle with length {length} and width {width} is: {area}")
