s = "IceCreAm"
s = list(s)
print(s)
vowels = set("aeiouAEIOU")
i = 0
j = len(s) - 1
while i < j:
    if s[i] in vowels and s[j] in vowels:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
    elif s[i] in vowels and s[j] not in vowels:
        j -= 1
    elif s[j] in vowels and s[i] not in vowels:
        i += 1
    else:
        i += 1
        j -= 1

print("".join(s))
