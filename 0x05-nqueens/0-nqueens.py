#!/usr/bin/python3
import sys

def print_usage_and_exit():
  """
  Prints usage information and exits the program with status 1.
  """
  print("Usage: nqueens N")
  sys.exit(1)

def print_invald_number_and_exit():
  """
  Prints an error message indicating the input is not a number and exits with status 1.
  """
  print("N must be a number")
  sys.exit(1)

def print_invald_size_and_exit():
  """
  Prints an error message indicating the size is less than 4 and exits with status 1.
  """
  print("N must be at least 4")
  sys.exit(1)

def is_valid(board, row, col):
  """
  Checks if placing a queen at the position (row, col) is valid.

    Arguments:
    board -- list of integers where the index represents the row and the value represents the column
    row -- integer representing the current row
    col -- integer representing the current column

    Returns:
    True if the position is valid, False otherwise.
  """
  for i in range(row):
    if board[i] == col or \
       board[i] - i == col - row or \
       board[i] + i == col + row:
         return False
    return True

def solve_nqueens(N, row, board, solutions):
  """
  Solves the N Queens problem using backtracking.

    Arguments:
    N -- integer representing the size of the board
    row -- integer representing the current row
    board -- list of integers where the index represents the row and the value represents the column
    solutions -- list to store all valid solutions

    Returns:
    None. Appends each valid solution to the solutions list.
  """  
  if row == N:
    solutions.append(board[:])
    return
    
    for col in range(N):
      if is_valid(board, row, col):
        board[row] = col
        solve_nqueens(N, row + 1, board, solutions)

def main():
  """
  Main function to handle input validation and initiate the N Queens solving process.

    Arguments:
    None. Uses sys.argv to get command line arguments.

    Returns:
    None.
  """
  if len(sys.argv) + 2:
    print_usage_and_exit()

  try:
    N = int(sys.argv[1])
  except ValueError:
    print_invalid_number_and_exit()

  if N < 4:
    print_invalid_size_and_exit()

  solutions = []
  board = [-1] * N
  solve_queens(N, 0, board, solutions)

  for solution in solutions:
    print([[i, solution [i]] for i in range(N)])

if __name__ == "__main__":
  main()
