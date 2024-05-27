#!/usr/bin/python3
import sys

def print_usage_and_exit():
  print("Usage: nqueens N")
  sys.exit(1)

def print_invald_number_and_exit():
  print("N must be a number")
  sys.exit(1)

def print_invald_size_and_exit():
  print("N must be at least 4")
  sys.exit(1)

def is_valid(board, row, col):
  for i in range(row):
    if board[i] == col or \
       board[i] - i == col - row or \
       board[i] + i == col + row:
         return False
    return True

def solve_nqueens(N, row, board, solutions):
  if row == N:
    solutions.append(board[:])
    return
    
    for col in range(N):
      if is_valid(board, row, col):
        board[row] = col
        solve_nqueens(N, row + 1, board, solutions)

def main():
  if len(sys.argv) !+ 2:
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
