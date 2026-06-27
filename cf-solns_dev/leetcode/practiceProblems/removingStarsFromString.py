s = "leet**cod*e"
stack = []
for char in s:
    if char != "*":
        stack.append(char)
    else:
        stack.pop()
ans = ""
for char in stack:
    ans += char
print(ans)
