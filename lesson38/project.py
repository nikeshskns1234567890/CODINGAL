# Swapping three numbers

print("Swapping three numbers example")

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore Swapping:")
print("a =", a, "b =", b, "c =", c)

# Swapping (a → b, b → c, c → a)
a, b, c = b, c, a

print("\nAfter Swapping:")
print("a =", b, "b =", c, "c =", a)
