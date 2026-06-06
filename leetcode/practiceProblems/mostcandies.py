candies = [2,3,5,1,3]
extraCandies = 3
i = 0
maxi = max(candies)
outList = []
for candy in candies:
    if candy + extraCandies >= maxi:
        outList.append(True)
    else:
        outList.append(False)

print(outList)