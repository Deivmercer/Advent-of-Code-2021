input_file = "input.txt"
with open(input_file) as input_file:
    input_file_rows = input_file.readlines()

# Of course the previous solution has become too slow

template = input_file_rows[0].strip()
pairs = dict()
for i, element in enumerate(template[:-1]):
    pair = element + template[i + 1]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1
insertion_rules = dict()
for row in input_file_rows[2:]:
    rule = row.strip().split(" -> ")
    insertion_rules[rule[0]] = rule[1]

for _ in range(40):
    new_pairs = dict()
    for pair, count in pairs.items():
        element = insertion_rules[pair[0] + pair[1]]
        pair_1 = pair[0] + element
        if pair_1 in new_pairs:
            new_pairs[pair_1] += count
        else:
            new_pairs[pair_1] = count
        pair_2 = element + pair[1]
        if pair_2 in new_pairs:
            new_pairs[pair_2] += count
        else:
            new_pairs[pair_2] = count
    pairs = new_pairs

char_counter = dict()
for pair, counter in pairs.items():
    if pair[0] in char_counter:
        char_counter[pair[0]] += counter
    else:
        char_counter[pair[0]] = counter
char_counter[template[-1]] += 1
print(max(char_counter.values()) - min(char_counter.values()))
