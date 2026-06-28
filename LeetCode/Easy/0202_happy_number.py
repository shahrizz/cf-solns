h = {}


def isHappy(n):
    if n not in h:
        h[n] = 1
    else:
        return False
    digits = [int(d) for d in str(n)]
    if digits == [1]:
        return True
    newSum = 0
    for digit in digits:
        newSum += pow(digit, 2)

    return isHappy(newSum)
