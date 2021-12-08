file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

row_list = [row.strip() for row in input_file_rows]
total = 0
result = 0
for row in row_list:
    number_dict = dict([(i, set()) for i in range(10)])
    unique_signal = row.split(" | ")[0].split(" ")
    output_values = row.split(" | ")[1].split(" ")
    five_segments = []
    six_segments = []
    for signal in unique_signal:
        if len(signal) == 2:
            number_dict[1].update(signal)
        elif len(signal) == 3:
            number_dict[7].update(signal)
        elif len(signal) == 4:
            number_dict[4].update(signal)
        elif len(signal) == 7:
            number_dict[8].update(signal)
        elif len(signal) == 5:
            five_segments += [set(signal)]
        elif len(signal) == 6:
            six_segments += [set(signal)]
    left_side = number_dict[4].intersection(number_dict[7].union(number_dict[1]))
    upper = number_dict[7].difference(left_side)
    middle_column = five_segments[0].intersection(five_segments[1].intersection(five_segments[2]))
    middle_column_2 = six_segments[0].intersection(six_segments[1].intersection(six_segments[2]))
    middle = middle_column.difference(middle_column_2)
    number_dict[0] = number_dict[8].difference(middle)
    six_segments.remove(number_dict[0])
    number_dict[3] = middle_column.union(left_side)
    five_segments.remove(number_dict[3])
    number_dict[9] = number_dict[4].union(middle_column)
    six_segments.remove(number_dict[9])
    number_dict[6] = six_segments[0]
    lower_right = number_dict[8].difference(number_dict[9])
    number_dict[5] = number_dict[6].difference(lower_right)
    five_segments.remove(number_dict[5])
    number_dict[2] = five_segments[0]
    actual_number = ""
    for value in output_values:
        value_set = set(value)
        for number, segments in number_dict.items():
            if segments == value_set:
                actual_number += str(number)
                break
    result += int(actual_number)

print(result)
