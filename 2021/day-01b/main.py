import math

file_name = "input.txt"
with open(file_name, "r") as input_file:
    input_file_rows = input_file.readlines()

list_len = math.ceil(len(input_file_rows)/3)
sum_list = [int(input_file_rows[0])] * 3
for index, row in enumerate(input_file_rows[1:], start=1):
    sum_list[index] += int(row)
    sum_list[index + 1] += int(row)
    sum_list += [int(row)]

count = 0
for index, element in enumerate(sum_list[2:len(sum_list) - 2]):
    if sum_list[index] > sum_list[index - 1]:
        count += 1
print(count)
