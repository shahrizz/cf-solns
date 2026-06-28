t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    ans = 0
    cost = 1

    while cost <= n:
        take = min(k, n // cost)
        ans += take
        n -= take * cost
        cost <<= 1

    print(ans)
