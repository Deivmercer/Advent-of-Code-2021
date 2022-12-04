import re

file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

horizontal = 0
depth = 0
for row in input_file_rows:
    regex = re.search("^(\\w+) (\\d)$", row)
    if regex.group(1) == "forward":
        horizontal += int(regex.group(2))
    elif regex.group(1) == "down":
        depth += int(regex.group(2))
    else:
        depth -= int(regex.group(2))
print(horizontal * depth)
