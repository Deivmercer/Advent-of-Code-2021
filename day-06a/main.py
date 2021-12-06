file_name = "input.txt"
with open(file_name) as input_file:
    file_content = input_file.readlines()

fish_list = [int(fish) for fish in file_content[0].split(',')]
for i in range(80):
    for index, timer in enumerate(fish_list):
        if timer == 0:
            fish_list[index] = 6
            fish_list += [9]
        else:
            fish_list[index] = timer - 1

print(len(fish_list))
