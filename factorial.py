def factorial(n):
    if n < 0:
        return None  #Negative number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5

print(f"Factorial of {n} is {factorial(n)}")