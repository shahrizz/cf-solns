x = 11
x = str(x)
i = 0
j = len(x) - 1
ans = True
while i < j:
    if x[i] != x[j]:
        ans = False
        break
    i += 1
    j -= 1
print(ans)
