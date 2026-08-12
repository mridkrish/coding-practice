n = int(input("Enter the size of the matrix: "))

for i in range(2*n-1):

    for j in range(2*n-1):

        minDist = min(i,j,((2 * n - 2) - i),((2 * n - 2) - j))

        print(n - minDist, end=" ")

    print()