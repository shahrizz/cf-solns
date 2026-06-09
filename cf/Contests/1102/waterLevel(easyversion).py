# n = 5
# h = [5, 3, 1, 5, 2]
# i = 1
# print(h[i % n])


t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    ans = []

    for start in range(n):
        cur = 0

        mn = 1000000000
        j = (start + 1) % n

        while j != start:
            edge = (j - 1 + n) % n
            mn = min(mn, h[edge])
            cur += mn
            j = (j + 1) % n

        ans.append(cur)

    print(*ans)
