flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2
i = 0
while i < len(flowerbed):
    if n == 0:
        break
    if i == (len(flowerbed) - 1) and flowerbed[i] == 0 and flowerbed[i - 1] != 1:
        flowerbed[i] = 1
        n -= 1
    if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] != 1:
        flowerbed[i] = 1
        n -= 1
    if flowerbed[i] == 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
        flowerbed[i] = 1
        n -= 1
    i += 1

if n == 0:
    print(True)
else:
    print(False)
