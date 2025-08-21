from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the given Sudoku puzzle by filling the empty cells in-place.
        Uses backtracking with row/column/box constraints.
        """

        # Track used numbers in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Keep track of empty cells that need filling
        empties = []

        # Step 1: Initialize sets with already filled numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    # Remember empty cell
                    empties.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        # Step 2: Backtracking function
        def backtrack(idx=0):
            # Base case: all empty cells are filled
            if idx == len(empties):
                return True

            r, c = empties[idx]        # Current empty cell
            b = (r // 3) * 3 + (c // 3)  # Box index (0-8)

            # Try placing numbers 1-9
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    # Place num tentatively
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    # Move to next empty cell
                    if backtrack(idx + 1):
                        return True

                    # Undo placement (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            # No valid number fits here → trigger backtrack
            return False

        # Step 3: Start recursion
        backtrack()
