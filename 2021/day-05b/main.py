import re

file_name = "input.txt"
with open(file_name, 'r') as input_file:
    input_file_rows = input_file.readlines()

lines_diagram = dict()
dangerous_points_count = 0
for row in input_file_rows:
    starting_x = -1
    ending_x = -1
    starting_y = -1
    ending_y = -1
    regex = re.search("(\\d+),(\\d+) -> (\\d+),(\\d+)", row)
    coordinate_1 = (int(regex.group(1)), int(regex.group(2)))
    coordinate_2 = (int(regex.group(3)), int(regex.group(4)))
    if coordinate_1[0] != coordinate_2[0] and coordinate_1[1] != coordinate_2[1]:
        if coordinate_1[0] < coordinate_2[0]:
            starting_x = coordinate_1[0]
            ending_x = coordinate_2[0] + 1
            starting_y = coordinate_1[1]
            ending_y = coordinate_2[1] + 1
        else:
            starting_x = coordinate_2[0]
            ending_x = coordinate_1[0] + 1
            starting_y = coordinate_2[1]
            ending_y = coordinate_1[1] + 1
        for w in range(ending_x - starting_x):
            if starting_y < ending_y:
                position = (starting_x + w, starting_y + w)
            else:
                position = (starting_x + w, starting_y - w)
            if position in lines_diagram:
                lines_diagram[position] += 1
                if lines_diagram[position] == 2:
                    dangerous_points_count += 1
            else:
                lines_diagram[position] = 1
    else:
        if coordinate_1[0] < coordinate_2[0]:
            starting_x = coordinate_1[0]
            ending_x = coordinate_2[0] + 1
        elif coordinate_1[0] > coordinate_2[0]:
            starting_x = coordinate_2[0]
            ending_x = coordinate_1[0] + 1
        elif coordinate_1[1] < coordinate_2[1]:
            starting_y = coordinate_1[1]
            ending_y = coordinate_2[1] + 1
        elif coordinate_1[1] > coordinate_2[1]:
            starting_y = coordinate_2[1]
            ending_y = coordinate_1[1] + 1
        for i in range(starting_x, ending_x):
            if (i, coordinate_1[1]) in lines_diagram:
                lines_diagram[(i, coordinate_1[1])] += 1
                if lines_diagram[(i, coordinate_1[1])] == 2:
                    dangerous_points_count += 1
            else:
                lines_diagram[(i, coordinate_1[1])] = 1
        for j in range(starting_y, ending_y):
            if (coordinate_1[0], j) in lines_diagram:
                lines_diagram[(coordinate_1[0], j)] += 1
                if lines_diagram[(coordinate_1[0], j)] == 2:
                    dangerous_points_count += 1
            else:
                lines_diagram[(coordinate_1[0], j)] = 1

print(dangerous_points_count)
