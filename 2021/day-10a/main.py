file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
error_score = 0
for row in input_file_rows:
    char_list = ""
    for char in row.strip():
        if char in {'(', '[', '{', '<'}:
            char_list += char
        else:
            if char_list[-1] == '(':
                if char != ')':
                    error_score += score_dict[char]
                    break
                else:
                    char_list = char_list[:-1]
            elif char_list[-1] == '[':
                if char != ']':
                    error_score += score_dict[char]
                    break
                else:
                    char_list = char_list[:-1]
            elif char_list[-1] == '{':
                if char != '}':
                    error_score += score_dict[char]
                    break
                else:
                    char_list = char_list[:-1]
            elif char_list[-1] == '<':
                if char != '>':
                    error_score += score_dict[char]
                    break
                else:
                    char_list = char_list[:-1]
print(error_score)
