prices = [7, 1, 5, 3, 6, 4]
bPricemin = 10000
i = 0
totalProfit = 0
while i < len(prices):
    bPrice = prices[i]
    if bPrice < bPricemin:
        bPricemin = bPrice
    elif (bPrice - bPricemin) > totalProfit:
        totalProfit = bPrice - bPricemin
    i += 1

return totalProfit
