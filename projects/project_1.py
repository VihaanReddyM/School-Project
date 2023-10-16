
values = [int(input("Enter the value for x: ")), int(input("Enter the value for y: ")]

print("Before Swap:")
print("x =", values[0])
print("y =", values[1])

values[0], values[1] = values[1], values[0]

print("After Swap:")
print("x =", values[0])
print("y =", values[1])
