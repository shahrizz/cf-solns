# n = 5
# a = [1, 4, 5, 2, 6]
# result = 0
# for num in a:
#     result ^= num

# print(result)
import sys

MOD = 998244353


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx : idx + n]
        idx += n

        if n == 1:
            out.append("0")
            continue

        total_xor = 0
        for x in a:
            total_xor ^= x

        if total_xor == 0:
            out.append("1")
        else:
            ans = 0
            for x in a:
                if (total_xor ^ x) < x:
                    ans += 1
            out.append(str(ans % MOD))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
