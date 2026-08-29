class Solution:
    def solveNQueens(self, n):

        result = []

        board = [["."] * n for _ in range(n)]

        def isSafe(row, col):

            # Check same column
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            # Check upper-left diagonal
            r = row - 1
            c = col - 1

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Check upper-right diagonal
            r = row - 1
            c = col + 1

            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def backtrack(row):

            # All queens are placed
            if row == n:
                arrangement = []

                for r in board:
                    arrangement.append("".join(r))

                result.append(arrangement)
                return

            # Try every column in this row
            for col in range(n):

                if isSafe(row, col):

                    # Choose
                    board[row][col] = "Q"

                    # Explore
                    backtrack(row + 1)

                    # Undo
                    board[row][col] = "."

        backtrack(0)

        return result