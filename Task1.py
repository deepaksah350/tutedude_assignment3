n = int(input("enter a number: "))
def fn(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fn(n-1)

result = n*fn(n-1)
print("factorial of", n, "is: ", result)