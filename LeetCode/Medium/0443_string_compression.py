# chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
# h = {}
# for char in chars:
#     if char not in h:
#         h[char] = 1
#     else:
#         h[char] += 1

# corespond_key = list(h.keys())
# corespond_val = list((h.values()))
# print(corespond_key)
chars = ["a", "a", "b", "b", "c", "c", "c"]
answer = []

current = chars[0]
count = 1

for i in range(1, len(chars)):
    if chars[i] == current:
        count += 1
    else:
        answer.append(current)

        if count > 1:
            for digit in str(count):
                answer.append(digit)

        current = chars[i]
        count = 1

print(answer)
