file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

bit_count = [[0, 0] for bit in input_file_rows[0][:len(input_file_rows[0]) - 1]]
for row in input_file_rows:
    for pos, bit in enumerate(row[:len(input_file_rows[0]) - 1]):
        if bit == '0':
            bit_count[pos][0] += 1
        else:
            bit_count[pos][1] += 1

gamma = ""
epsilon = ""
for bit in bit_count:
    if bit[0] > bit[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)
print(gamma_dec * epsilon_dec)
