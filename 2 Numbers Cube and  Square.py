n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second Number: "))

if n1 > n2:
    print("Smaller Number Square: ", n2 ** 2)
    print("Greater number Cube: ", n1 ** 3)

elif n2 > n1:
    print("Smaller Number Square: ", n1 ** 2)
    print("Greater number Cube: ", n2 ** 3)

elif n1 == n2:
    print("Both numbers are equal!")
    print("Square: ", n1 ** 2)
    print("Square Root: ", n1 ** 0.5)
    print("CubeRoot: ", n1 ** (1 / 3))

else:
    print("Invalid Input")
