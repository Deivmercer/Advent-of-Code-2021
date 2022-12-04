file_name = "input.txt"
with open(file_name) as input_file:
    input_file_rows = input_file.readlines()

path_risk = [0] * len(input_file_rows[0].strip())
for i, risk in list(enumerate(input_file_rows[-1].strip()))[::-1]:
    path_risk[i] = int(risk)
    if i != len(path_risk) - 1:
        path_risk[i] += path_risk[i + 1]

for i, row in list(enumerate(input_file_rows[:-1]))[::-1]:
    new_path_risk = [0] * len(path_risk)
    for j, risk_level in list(enumerate(row.strip()))[::-1]:
        if j == len(row.strip()) - 1:
            new_path_risk[j] = int(risk_level) + path_risk[j]
        else:
            risk = int(risk_level) + path_risk[j]
            if int(risk_level) + new_path_risk[j + 1] < risk:
                risk = int(risk_level) + new_path_risk[j + 1]
            new_path_risk[j] = risk
    path_risk = new_path_risk

# Works just fine with the example but with the actual input the result is slightly wrong
print(path_risk[0] - int(input_file_rows[0][0]))
