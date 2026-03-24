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

def bin_search(arr, target):
    mid = len(arr) // 2
    while target >= arr(mid):
        

t = int(input())
answers = []
while t > 0:

    n = int(input())
    i = 1
    ai = []
    bi = []

    temp = list(map(int, input().split()))
    while i <= n:
        ai.append(temp[i-1])
        i = i + 1

    i = 1

    temp = list(map(int, input().split()))
    while i <= n:
        bi.append(temp[i-1])
        i = i + 1

    def calck(x, a, b):
        prefix = [0]
        for value in b:
            prefix.append(prefix[-1] + value)
        swordtotal = 0
        for elem in a:
            if elem >= x:
                swordtotal= swordtotal + 1
        
        

    x = 0
    maxscore = 0
    for x in ai:
        currentScore = x*(calck(x, ai, bi))
        if currentScore >= maxscore:
            maxscore = currentScore
        x = x + 1

    answers.append(maxscore)

    t = t - 1
for ans in answers:
    print(ans)