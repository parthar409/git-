def grasshopper_jump(x, k):
  """
  This function finds the smallest number of moves it takes a grasshopper to reach point x from 0,
  where each move is an integer distance, not divisible by k, to the left or to the right.

  Args:
    x: The endpoint the grasshopper wants to reach.
    k: The constraint on the jumps.

  Returns:
    A tuple of the smallest number of moves and a list of the moves.
  """

  # Initialize the number of moves and the list of moves.
  num_moves = 0
  moves = []

  # While the grasshopper is not at the endpoint, add a move to the list of moves.
  while x != 0:
    # Find the smallest move that will bring the grasshopper closer to the endpoint.
    move = min(abs(x), abs(k - x))

    # Add the move to the list of moves.
    moves.append(move)

    # Update the grasshopper's position.
    x += move

    # Increment the number of moves.
    num_moves += 1

  # Return the number of moves and the list of moves.
  return num_moves, moves


def main():
  """
  This function reads the input and prints the output for the Grasshopper Jump problem.
  """

  # Read the number of testcases.
  t = int(input())

  # Loop over the testcases.
  for _ in range(t):
    # Read the endpoint and the constraint on the jumps.
    x, k = map(int, input().split())

    # Find the smallest number of moves and the list of moves.
    num_moves, moves = grasshopper_jump(x, k)

    # Print the number of moves.
    print(num_moves)

    # Print the list of moves.
    print(' '.join(map(str, moves)))


if __name__ == '__main__':
  main()
