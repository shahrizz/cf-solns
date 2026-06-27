nums = [8, 1, 7, 2, 6, 3, 5, 4]
# we want the final number to be as small as possible
# meaning in greedy sense we need ai+1 to be as small as possible
# we need each element to be as small as possible
# 5 1 4
# 6 1 2 3
# 3 1 5 2
# 8 2 1 7
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    stack = []

    for x in a:
        stack.append(x)

        while len(stack) >= 2 and stack[-2] > stack[-1]:
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)

    print(max(stack))
