class Solution:
    def solveNQueens(self, n: int):
        rowf = [False] * n
        colf = [False] * n
        t1df = [False] * (2 * n + 1)
        t2df = [False] * (2 * n + 1)