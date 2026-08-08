n = int(input("Enter the number of rows: "))

for i in range(n+1):
    # Left stars
    for j in range(i):
        print("*", end="")

    # Spaces
    for k in range(2*(n-i)):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*", end="")

    print()

for i in range(n+1):
    # Left stars
    for j in range((n-i)):
        print("*", end="")

    # Spaces
    for k in range(2*i):
        print(" ", end="")

    # Right stars
    for j in range((n-i)):
        print("*", end="")

    print()