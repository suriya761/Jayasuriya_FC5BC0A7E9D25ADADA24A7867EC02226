
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
n=int(input("Enter a number you want to find the factorial:"))
r=factorial(n)
print(f"The factorial for {n} is {r}")