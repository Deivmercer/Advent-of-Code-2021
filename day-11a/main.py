flash_count = 0


def increase_energy(octopuses, i, j, flashing):
    if octopuses[i][j] == 9:
        octopuses[i][j] = 0
        flashing.append((i, j))
    else:
        octopuses[i][j] += 1


def flash(octopuses, flashing):
    global flash_count
    new_flashing = list()
    for (i, j) in flashing:
        flash_count += 1
        if i > 0:
            if j > 0 and octopuses[i - 1][j - 1] != 0:
                increase_energy(octopuses, i - 1, j - 1, new_flashing)
            if octopuses[i - 1][j] != 0:
                increase_energy(octopuses, i - 1, j, new_flashing)
            if j < len(octopuses[0]) - 1 and octopuses[i - 1][j + 1] != 0:
                increase_energy(octopuses, i - 1, j + 1, new_flashing)
        if j > 0 and octopuses[i][j - 1] != 0:
            increase_energy(octopuses, i, j - 1, new_flashing)
        if j < len(octopuses[0]) - 1 and octopuses[i][j + 1] != 0:
            increase_energy(octopuses, i, j + 1, new_flashing)
        if i < len(octopuses) - 1:
            if j > 0 and octopuses[i + 1][j - 1] != 0:
                increase_energy(octopuses, i + 1, j - 1, new_flashing)
            if octopuses[i + 1][j] != 0:
                increase_energy(octopuses, i + 1, j, new_flashing)
            if j < len(octopuses[0]) - 1 and octopuses[i + 1][j + 1] != 0:
                increase_energy(octopuses, i + 1, j + 1, new_flashing)
    if new_flashing:
        flash(octopuses, new_flashing)


file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

octopuses = [[int(octopus) for octopus in row.strip()] for row in input_file_rows]

for step in range(100):
    flashing = list()
    for i, row in enumerate(octopuses):
        for j, _ in enumerate(row):
            increase_energy(octopuses, i, j, flashing)
    flash(octopuses, flashing)
print(flash_count)
