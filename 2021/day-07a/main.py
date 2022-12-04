file_name = "input.txt"
with open(file_name) as input_file:
    input_file_content = input_file.readline()

crab_position = input_file_content.split(',')
distance_dict = dict([(int(position), 0) for position in crab_position])
for position in distance_dict.keys():
    for crab in crab_position:
        distance_dict[position] += int(crab) - position if int(crab) >= position else position - int(crab)

lower_cost = 99999999999
for position, value in distance_dict.items():
    if value < lower_cost:
        lower_cost = value
print(lower_cost)
