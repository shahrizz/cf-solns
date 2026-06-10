s = "abc"
t = "ahbgdc"
i = 0
j = 0
while i < len(s):
    if j > len(t):
        print(False)
        break
    if s[i] == s[j]:
        i += 1
        j += 1
    else:
        j += 1
