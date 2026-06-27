text = "loonbalxballpoon"

h = {}

for letter in text:
    h[letter] = h.get(letter, 0) + 1

print(
    min(
        h.get("b", 0),
        h.get("a", 0),
        h.get("l", 0) // 2,
        h.get("o", 0) // 2,
        h.get("n", 0),
    )
)
