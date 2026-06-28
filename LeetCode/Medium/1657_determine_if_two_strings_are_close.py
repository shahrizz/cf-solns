word1 = "abc"
word2 = "bca"
h1 = {}
h2 = {}

for letter in word1:
    if letter in h1:
        h1[letter] += 1
    else:
        h1[letter] = 1

for letter in word2:
    if letter in h2:
        h2[letter] += 1
    else:
        h2[letter] = 1


# print(h1 == h2)
# values_h1 = h1.values()
# values_h2 = h2.values()
# print(values_h1 == values_h2)
set(h1.keys()) == set(h2.keys())
sorted(h1.values()) == sorted(h2.values())
