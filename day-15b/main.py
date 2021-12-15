file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

tmp_cave_map = list()
for row in input_file_rows:
    map_row = list()
    for w in range(5):
        map_row += [int(char) + w if int(char) + w <= 9 else (int(char) + w) % 9 for char in row.strip()]
    tmp_cave_map += [map_row]
cave_map = tmp_cave_map.copy()
for w in range(1, 5):
    for row in tmp_cave_map:
        cave_map.append([level + w if level + w <= 9 else (level + w) % 9 for level in row])

path_risk = [0] * len(cave_map[0])
for i, risk in list(enumerate(cave_map[-1]))[::-1]:
    path_risk[i] = risk
    if i != len(path_risk) - 1:
        path_risk[i] += path_risk[i + 1]

for i, row in list(enumerate(cave_map[:-1]))[::-1]:
    new_path_risk = [0] * len(path_risk)
    for j, risk_level in list(enumerate(row))[::-1]:
        if j == len(row) - 1:
            new_path_risk[j] = risk_level + path_risk[j]
        else:
            risk = risk_level + path_risk[j]
            if risk_level + new_path_risk[j + 1] < risk:
                risk = risk_level + new_path_risk[j + 1]
            new_path_risk[j] = risk
    path_risk = new_path_risk

# Works just fine with the example but with the actual input the result is slightly wrong :/
print(path_risk[0] - int(input_file_rows[0][0]))
