from functools import reduce

# Function to generate Fibonacci numbers
fibonacci = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1])

# Create a Fibonacci series with 50 elements
result = fibonacci(50)

print(result)