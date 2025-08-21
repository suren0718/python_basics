def diagonal_triangle(n):
    # Step 1: Fill diagonals of an n x n square
    mat = [[0]*n for _ in range(n)]
    num = 1
    for d in range(2*n-1):
        if d % 2 == 0:  # even diagonal → DOWN
            c = min(d, n-1)
            r = d - c
            while c >= 0 and r < n:
                mat[r][c] = num
                num += 1
                r += 1
                c -= 1
        else:  # odd diagonal → UP
            r = min(d, n-1)
            c = d - r
            while r >= 0 and c < n:
                mat[r][c] = num
                num += 1
                r -= 1
                c += 1

    # Step 2: Print only lower triangle
    for i in range(n):
        print(" ".join(str(mat[i][j]) for j in range(i+1)))


diagonal_triangle(5)
