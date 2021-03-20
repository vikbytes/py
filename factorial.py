# Recursive function to calculate the n:th factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1) * n
        return recurse

print(factorial(int(input)))
