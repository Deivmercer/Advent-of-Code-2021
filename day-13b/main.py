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
max_x = 0
max_y = 0
final_dots = set()
for dot in dots:
    if dot[0] > max_x:
        max_x = dot[0]
    if dot[1] > max_y:
        max_y = dot[1]
    final_dots.update([(dot[0], dot[1])])
for i in range(max_y + 1):
    line = ""
    for j in range(max_x + 1):
        if (j, i) in final_dots:
            line += "#"
        else:
            line += "."
    print(line)
