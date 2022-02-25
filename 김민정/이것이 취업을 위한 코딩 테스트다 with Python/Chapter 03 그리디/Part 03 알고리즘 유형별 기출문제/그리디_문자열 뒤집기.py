#1
input_data = input()

case_0, case_1 = 0, 0

if input_data[0] == '1':
    case_0 += 1
else:
    case_1 += 1

for i in range(len(input_data) - 1):
    if input_data[i] != input_data[i + 1]:
        if input_data[i] == '1':
            case_0 += 1
        else:
            case_1 += 1

print(min(case_0, case_1))

# 2
input_data = input()

count = 0
for i in range(len(input_data) - 1):
    if input_data[i] != input_data[i + 1]:
        count += 1
print((count + 1)//2)