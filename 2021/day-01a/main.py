file_name = "input.txt"
with open(file_name, "r") as input_file:
    input_file_rows = input_file.readlines()

count = 0
for index, row in enumerate(input_file_rows[1:], start=1):
    if int(row) > int(input_file_rows[index - 1]):
        count += 1

print(count)
