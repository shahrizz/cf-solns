# t = int(input())

# for _ in range(t):
#     n = int(input())
#     b = list(map(int, input().split()))

#     b = sorted(b, reverse=True)
#     x =
#     i = 2
#     while i < n:
#         if not b[i] == b[i - 2] % b[i - 1]:
#             print(-1)
#             break
#         i += 1

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    b.sort(reverse=True)

    if n == 2:
        print(b[0], b[1])
        continue

    ok = True
    i = 2

    while i < n:
        if b[i] != b[i - 2] % b[i - 1]:
            ok = False
            break
        i += 1

    if ok:
        print(b[0], b[1])
    else:
        print(-1)
