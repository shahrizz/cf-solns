# n = 310


# # 262+48
# # a is palindrome
# # b is div by 12
# def isPalindrome(x):
#     if x < 0 or (x % 10 == 0 and x != 0):
#         return False

#     rev = 0
#     while x > rev:
#         rev = rev * 10 + x % 10
#         x //= 10

#     return x == rev or x == rev // 10


# i = 1
# while (12 * i) < n:
#     b = 12 * i
#     a = n - b
#     if isPalindrome(a):
#         print(a)
#         print(b)
#         break
#     i += 1

t = int(input())

pal_rem = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None, 11]

for _ in range(t):
    n = int(input())

    r = n % 12

    if r == 10:
        a = 22
    else:
        a = pal_rem[r]

    if a is None or a > n:
        print(-1)
    else:
        print(a, n - a)
