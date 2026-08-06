n = int(input("Enter number of rows: "))

for i in range(n):

    for j in range (i+1):
        print(chr(ord('A') + n - 1 + j - i), end="")

    print()