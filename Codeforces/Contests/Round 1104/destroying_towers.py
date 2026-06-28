t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    mn = float("inf")

    for x in a:
        mn = min(mn, x)
        ans += mn

    print(ans)
