file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

dots = []
instructions = []
for row in input_file_rows:
    if row == '\n':
        continue
    if not row.startswith("fold"):
        dots += [list(map(int, row.strip().split(',')))]
    else:
        split = row.strip().split("fold along ")[1].split('=')
        instructions += [(split[0], int(split[1]))]

for instruction in instructions:
    if instruction[0] == 'x':
        for dot in dots:
            if dot[0] > instruction[1]:
                dot[0] = instruction[1] - (dot[0] - instruction[1])
    else:
        for dot in dots:
            if dot[1] > instruction[1]:
                dot[1] = instruction[1] - (dot[1] - instruction[1])
    break

final_dots = set((x, y) for [x, y] in dots)
print(len(final_dots))
