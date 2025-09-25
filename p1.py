def solve_n_queens(n):
    """
    Solves the N-Queens problem and returns a list of all distinct solutions.
    Each solution is represented as a list of strings, where 'Q' denotes a queen
    and '.' denotes an empty square.
    """
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        """
        Checks if placing a queen at board[row][col] is safe.
        """
        # Check this column on upper side
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper diagonal on left side
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Check upper diagonal on right side
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        return True

    def backtrack(row):
        """
        Recursive backtracking function to place queens.
        """
        if row == n:
            # All queens placed, add current board configuration to solutions
            current_solution = ["".join(r) for r in board]
            solutions.append(current_solution)
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'  # Place queen
                backtrack(row + 1)     # Recurse for the next row
                board[row][col] = '.'  # Backtrack: remove queen

    backtrack(0)  # Start placing queens from the first row (row 0)
    return solutions

if __name__ == "__main__":
    n = 4  # Example: Solve for 4 Queens
    all_solutions = solve_n_queens(n)

    if not all_solutions:
        print(f"No solutions found for {n}-Queens problem.")
    else:
        print(f"Found {len(all_solutions)} solutions for {n}-Queens problem:")
        for i, solution in enumerate(all_solutions):
            print(f"Solution {i + 1}:")
            for row_str in solution:
                print(row_str)
            print()
