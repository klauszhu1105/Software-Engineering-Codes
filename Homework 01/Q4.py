def fibonacci(n):
    fib_sequence = [1, 1]  
    for _ in range(n - 2): 
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Compute the first 100 Fibonacci numbers
fib_numbers = fibonacci(100)

# Print the results
for index, num in enumerate(fib_numbers, start=1):
    print(f"Fibonacci {index}: {num}")