#Write a Python program to create Fibonacci series up to n using Lambda. 

# Fibonacci series upto 2: 
# [0, 1] 
# Fibonacci series upto 5: 
# [0, 1, 1, 2, 3] 
# Fibonacci series upto 6: 
# [0, 1, 1, 2, 3, 5] 

fibonacci = lambda n: [] if n <= 0 else [0] if n == 1 else [0, 1] if n == 2 else \
    fibonacci(n - 1) + [fibonacci(n - 1)[-1] + fibonacci(n - 1)[-2]]
def display_fibonacci(n):
    series = fibonacci(n)
    print(f"Fibonacci series upto {n}:\n{series}\n")
    print(fibonacci)
num=int(input("Enter a number"))
display_fibonacci(num)
