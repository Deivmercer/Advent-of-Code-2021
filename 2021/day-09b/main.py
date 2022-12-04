def look_up(heightmap, basin_set, i, j):
    i -= 1
    if i >= 0 and heightmap[i][j] != 9 and (i, j) not in basin_set:
        basin_set.add((i, j))
        look_up(heightmap, basin_set, i, j)
        look_left(heightmap, basin_set, i, j)
        look_right(heightmap, basin_set, i, j)


def look_left(heightmap, basin_set, i, j):
    j -= 1
    if j >= 0 and heightmap[i][j] != 9 and (i, j) not in basin_set:
        basin_set.add((i, j))
        look_up(heightmap, basin_set, i, j)
        look_left(heightmap, basin_set, i, j)
        look_down(heightmap, basin_set, i, j)


def look_right(heightmap, basin_set, i, j):
    j += 1
    if j < len(row) and heightmap[i][j] != 9 and (i, j) not in basin_set:
        basin_set.add((i, j))
        look_up(heightmap, basin_set, i, j)
        look_right(heightmap, basin_set, i, j)
        look_down(heightmap, basin_set, i, j)


def look_down(heightmap, basin_set, i, j):
    i += 1
    if i < len(input_file_rows) and heightmap[i][j] != 9 and (i, j) not in basin_set:
        basin_set.add((i, j))
        look_left(heightmap, basin_set, i, j)
        look_right(heightmap, basin_set, i, j)
        look_down(heightmap, basin_set, i, j)


file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

heightmap = [[int(height) for height in row.strip()] for row in input_file_rows]
basin_size = []
for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
        lowest = True
        if i < len(input_file_rows) - 1 and height >= heightmap[i + 1][j]:
            lowest = False
        if j < len(row) - 1 and height >= heightmap[i][j + 1]:
            lowest = False
        if j > 0 and height >= heightmap[i][j - 1]:
            lowest = False
        if i > 0 and height >= heightmap[i - 1][j]:
            lowest = False
        if lowest:
            basin_set = {(i, j)}
            look_up(heightmap, basin_set, i, j)
            look_left(heightmap, basin_set, i, j)
            look_right(heightmap, basin_set, i, j)
            look_down(heightmap, basin_set, i, j)
            basin_size += [len(basin_set)]

basin_size.sort(reverse=True)
print(basin_size[0] * basin_size[1] * basin_size[2])
