file_name = "input.txt"
with open(file_name) as input_file:
    file_content = input_file.readlines()

# After almost 1 hour of execution and over 10GB of RAM eaten, I decided this doesn't work.
# R. I. P.
# fish_list = [int(fish) for fish in file_content[0].split(',')]
# for i in range(256):
#     for index, timer in enumerate(fish_list):
#         if timer == 0:
#             fish_list[index] = 6
#             fish_list += [9]
#         else:
#             fish_list[index] = timer - 1

fish_count = 0
timer_list = [0] * 10
for fish in file_content[0].split(','):
    timer_list[int(fish)] += 1
    fish_count += 1

previous_timer = 0
for i in range(256):
    timer_list[7] += timer_list[0]
    timer_list[9] = timer_list[0]
    fish_count += timer_list[0]
    for timer in range(1, 10)[::-1]:
        if timer == 9:
            previous_timer = timer_list[timer - 1]
            timer_list[timer - 1] = timer_list[timer]
            timer_list[timer] = 0
        else:
            swap = previous_timer
            previous_timer = timer_list[timer - 1]
            timer_list[timer - 1] = swap

print(fish_count)
