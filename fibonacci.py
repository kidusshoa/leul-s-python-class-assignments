def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input!"
    elif n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter the value of n: "))
print(f"The {n}th Fibonacci number is: {fibonacci_recursive(n)}")
