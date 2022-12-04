file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

heightmap = [[int(height) for height in row.strip()] for row in input_file_rows]
total_risk = 0
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
            total_risk += height + 1
print(total_risk)
