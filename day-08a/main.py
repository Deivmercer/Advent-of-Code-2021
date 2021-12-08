file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

digits_counter = 0
output_value_list = [[value for value in row.split('|')[1].strip().split(' ')] for row in input_file_rows]
for output_value_row in output_value_list:
    for output_value in output_value_row:
        if len(output_value) == 2 or len(output_value) == 3 or len(output_value) == 4 or len(output_value) == 7:
            digits_counter += 1
print(digits_counter)
