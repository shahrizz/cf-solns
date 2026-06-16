s = "   fly me   to   the moon  "
s = s.rstrip()
j = len(s) - 1
counter = 0
while True:
    if s[j] == " ":
        print(counter)
        break
    else:
        counter += 1
        j -= 1
