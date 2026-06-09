
t = int(input())
answers = []
for _ in range(t):
    a, b = map(int, input().split())

    def max_layers(white, dark):
        layers = 0
        need = 1
        turn_white = True

        while True:
            if turn_white:
                if white < need:
                    break
                white -= need
            else:
                if dark < need:
                    break
                dark -= need

            layers += 1
            need *= 2
            turn_white = not turn_white

        return layers

    answers.append(max(max_layers(a, b), max_layers(b, a)))

for ans in answers:
    print(ans)
