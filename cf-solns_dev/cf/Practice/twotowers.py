a = 3
b = 3
c = 6
d = 4

if a > b:
    temp = a
    a = b
    b = temp
    temp = c
    d = c
    d = temp

i = 0
while b < d:
    i = i + 1
    while a < c:
        i = i + 1
        if a == b:
            a = a + 1
            b = b + 1
        else:
            a = a + 1
    b = b + 1

if i != 0:
    i = i - 1

print(i)