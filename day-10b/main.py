file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

score_dict = {'(': 1, '[': 2, '{': 3, '<': 4}
score_list = []
for row in input_file_rows:
    char_list = ""
    counter = 0
    for char in row.strip():
        if char in {'(', '[', '{', '<'}:
            char_list += char
        else:
            if char_list[-1] == '(':
                if char != ')':
                    break
                else:
                    char_list = char_list[:-1]
            elif char_list[-1] == '[':
                if char != ']':
                    break
                else:
                    char_list = char_list[:-1]
            elif char_list[-1] == '{':
                if char != '}':
                    break
                else:
                    char_list = char_list[:-1]
            elif char_list[-1] == '<':
                if char != '>':
                    break
                else:
                    char_list = char_list[:-1]
        counter += 1
    if counter == len(row.strip()):
        score = 0
        for char in char_list[::-1]:
            score = score * 5 + score_dict[char]
        score_list.append(score)

score_list.sort()
print(score_list[int(len(score_list) / 2)])
