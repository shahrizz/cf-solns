def consecutiveSetBits(n):
    binn = bin(n)[2:]

    count = 0
    for i in range(len(binn) - 1):
        if binn[i] == "1" and binn[i + 1] == "1":
            count += 1

    return count == 1


n = 30
print(consecutiveSetBits(n))
