# n = 3
# a = [3, 1, 1, 2]
# # track winning or losing position...
# # last is always a losing position for person last played and winning for person who is about to play
# # tracker = [, 0] <- 1 means player would be better off playing and 0 means player would be worse of playing
# # more bennifical as index shifs from right to left
# # each step each player wants to

#!/usr/bin/env python3
import sys


def gameOfStones(n):
    """
    Determines the winner of the Game of Stones.
    Alice moves first. Available moves: remove 2, 3, or 5 stones.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # A player stuck with a number of stones where the remainder
    # modulo 7 is 0 or 1 is in a losing position.
    if n % 7 == 0 or n % 7 == 1:
        return "Bob"
    return "Alice"


def main():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # The first integer represents the number of test cases
    t = int(input_data[0])

    # Process each test case sequentially
    for i in range(1, t + 1):
        n = int(input_data[i])
        print(gameOfStones(n))


if __name__ == "__main__":
    main()
