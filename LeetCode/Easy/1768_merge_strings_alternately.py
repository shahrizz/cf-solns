word1 = "ab"
word2 = "pqrs"
i = 0
j = 0
final = ""
while i < len(word1) and j < len(word2):
    final += word1[i] + word2[j]
    i += 1
    j += 1
if i >= len(word1):
    final += word2[(j):]
elif j >= len(word2):
    final += word1[(i):]
