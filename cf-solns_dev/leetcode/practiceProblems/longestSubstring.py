s = "abcabcbb"
i = 0
j = 0
h = {}
max_size = 0

while j < len(s):
    if s[j] not in h:
        h[s[j]] = 1
        j += 1
        max_size = max(max_size, j - i)
    else:
        del h[s[i]]
        i += 1

print(max_size)
