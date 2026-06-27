# import sys
# input = sys.stdin.readline
# # a = [1, 3, 4]
# # x = 3
# # b = [2, 1, 1]
# # for elem in a:
# #     if elem < x:
# #         a.remove(elem)
# # swordtotal = len(a)
# # k = 0

# # for elem in b:
# #     if swordtotal < elem:
# #         break
# #     swordtotal = swordtotal - elem
# #     k = k + 1
# # print(k)
# t = int(input())
# answers = []
# for _ in range(t):
#     n = int(input())
#     i = 1
#     ai = list(map(int, input().split()))
#     bi = list(map(int, input().split()))
#     while i <= n:
#         ai = list(map(int, input().split()))
#         i = i + 1
#     i = 1
#     while i <= n:
#         bi = list(map(int, input().split()))
#         i = i + 1

#     def calck(x, a, b):
#         swordtotal = 0
#         for elem in a:
#             if elem >= x:
#                 swordtotal = swordtotal + 1
#         k = 0
#         for elem in b:
#             if swordtotal < elem:
#                 break
#             swordtotal = swordtotal - elem
#             k = k + 1
#         return k

#     x = 0
#     maxscore = 0
#     for x in ai:
#         currentScore = x*(calck(x, ai, bi))
#         if currentScore >= maxscore:
#             maxscore = currentScore
#         x = x + 1

# t = int(input())
# answers = []
# while t > 0:

#     n = int(input())
#     i = 1
#     ai = []
#     bi = []

#     # take ai input
#     temp = list(map(int, input().split()))
#     while i <= n:
#         ai.append(temp[i-1])
#         i = i + 1

#     i = 1

#     # take bi input
#     temp = list(map(int, input().split()))
#     while i <= n:
#         bi.append(temp[i-1])
#         i = i + 1

#     def calck(x, a, b):
#         for elem in a:
#             if elem < x:
#                 a.remove(elem)
#         swordtotal = len(a)
#         k = 0
#         for elem in b:
#             if swordtotal < elem:
#                 break
#             swordtotal = swordtotal - elem
#             k = k + 1
#         return k

#     x = 0
#     maxscore = 0
#     for x in ai:
#         currentScore = x*(calck(x, ai, bi))
#         if currentScore >= maxscore:
#             maxscore = currentScore
#         x = x + 1

#     answers.append(maxscore)

#     t = t - 1

# for ans in answers:
#     print(ans)


