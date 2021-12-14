from collections import Counter

input_file = "input.txt"
with open(input_file) as input_file:
    input_file_rows = input_file.readlines()

template = input_file_rows[0].strip()
insertion_rules = dict()
for row in input_file_rows[2:]:
    rule = row.strip().split(" -> ")
    insertion_rules[rule[0]] = rule[1]

for _ in range(10):
    new_polymer = template[0]
    for i, element in enumerate(template[1:], start=1):
        if i < len(template):
            new_polymer += insertion_rules[template[i - 1] + template[i]] + template[i]
    template = new_polymer
counter = Counter(template).most_common()
print(counter[0][1] - counter[-1][1])
