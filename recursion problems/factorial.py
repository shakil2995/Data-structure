# Write a function that calculates the factorial of a non-negative integer n. The factorial of n is the product of all positive integers less than or equal to n. For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n*int(factorial(n-1))


print(factorial(10))
