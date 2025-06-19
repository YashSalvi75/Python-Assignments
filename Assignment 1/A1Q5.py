def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    print(f"Factorial of {n} = {result}")

 
factorial(5)
