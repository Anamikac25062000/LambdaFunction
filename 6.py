#Write a Python program to create Fibonacci series up to n using Lambda. 

# Fibonacci series upto 2: 
# [0, 1] 
# Fibonacci series upto 5: 
# [0, 1, 1, 2, 3] 
# Fibonacci series upto 6: 
# [0, 1, 1, 2, 3, 5] 

fibonacci_series = lambda n: [] if n <= 0 else [0] if n == 1 else [0, 1] if n == 2 else \
    fibonacci_series(n - 1) + [fibonacci_series(n - 1)[-1] + fibonacci_series(n - 1)[-2]]

def display_fibonacci_series(n):
    series = fibonacci_series(n)
    print(f"Fibonacci series upto {n}:\n{series}\n")

display_fibonacci_series(2)
display_fibonacci_series(5)
display_fibonacci_series(6)
