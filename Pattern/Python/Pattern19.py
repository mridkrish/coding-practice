n = int(input("Enter number of rows: "))

for i in range(n):
    # Left stars
    for j in range(n - i):
        print("*", end="")

    # Spaces
    for k in range(i * 2 + 1):
        print(" ", end="")

    # Right stars
    for j in range(n - i):
        print("*", end="")

    print()

for i in range(n - 1, -1, -1):
    # Left stars
    for j in range(n - i):
        print("*", end="")

    # Spaces
    for k in range(i * 2 + 1):
        print(" ", end="")

    # Right stars
    for j in range(n - i):
        print("*", end="")

    print()