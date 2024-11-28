def gcdFinder(a,b):
    while b != 0:
        a, b = b, a%b
    return a

n1 = int(input("First number: "))
n2 = int(input("Second number: "))

result = gcdFinder(n1,n2)
print(f"The GCD is: {result}")