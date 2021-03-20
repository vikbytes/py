# Ackermann function
# https://en.wikipedia.org/wiki/Ackermann_function
def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

m = int(input("m: "))
n = int(input("n: "))

print("Result: ", ackermann(m,n))