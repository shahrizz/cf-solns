# haystack = "sadbutsad"
# needle = "sad"
# diff = len(haystack) - len(needle)
# i = 0
# j = 0
# ans = -1
# while i < diff and j < len(needle):
#     if haystack[i] == needle[j]:
#         i += 1
#         j += 1
#         ans = i
#     else:
#         j = 0
#         i += 1

# if not j == len(needle):
#     ans = -1
#     print(ans)
# else:
#     print(ans)

haystack = "sadbutsad"
needle = "sad"

diff = len(haystack) - len(needle)
ans = -1

for i in range(diff + 1):
    j = 0

    while j < len(needle) and haystack[i + j] == needle[j]:
        j += 1

    if j == len(needle):
        ans = i
        break

print(ans)
