def isPower(n):
    if n == 1:
        return True
    if n < 1:
        return False
    n = n / 2
    return isPower(n)


print(isPower(500))
