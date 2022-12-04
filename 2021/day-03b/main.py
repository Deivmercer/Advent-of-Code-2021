def count_bit(binary_number):
    bit_count = [[0, 0] for _ in binary_number[0][:len(binary_number[0]) - 1]]
    for row in binary_number:
        for pos, bit in enumerate(row[:len(binary_number[0]) - 1]):
            if bit == '0':
                bit_count[pos][0] += 1
            else:
                bit_count[pos][1] += 1
    return bit_count


file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

oxygen_bit_list = input_file_rows
index = 0
while len(oxygen_bit_list) > 1:
    tmp_oxygen_list = list()
    bit_count = count_bit(oxygen_bit_list)
    for binary_number in oxygen_bit_list:
        if bit_count[index][0] > bit_count[index][1] and binary_number[index] == '0':
            tmp_oxygen_list += [binary_number]
        elif bit_count[index][1] >= bit_count[index][0] and binary_number[index] == '1':
            tmp_oxygen_list += [binary_number]
    oxygen_bit_list = tmp_oxygen_list
    index += 1

co2_bit_list = input_file_rows
index = 0
while len(co2_bit_list) > 1:
    tmp_co2_list = list()
    bit_count = count_bit(co2_bit_list)
    for binary_number in co2_bit_list:
        if bit_count[index][0] <= bit_count[index][1] and binary_number[index] == '0':
            tmp_co2_list += [binary_number]
        elif bit_count[index][1] < bit_count[index][0] and binary_number[index] == '1':
            tmp_co2_list += [binary_number]
    co2_bit_list = tmp_co2_list
    index += 1

oxygen_dec = int(oxygen_bit_list[0], 2)
co2_dec = int(co2_bit_list[0], 2)
print(oxygen_dec * co2_dec)
