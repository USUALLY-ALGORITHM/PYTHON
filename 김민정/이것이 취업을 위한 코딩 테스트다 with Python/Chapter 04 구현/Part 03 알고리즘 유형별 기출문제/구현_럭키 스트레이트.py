N = input()
N_len = len(N)

sum_1, sum_2 = 0, 0
for i in range(0, N_len // 2):
    sum_1 += int(N[i])

for i in range(N_len // 2, N_len):
    sum_2 += int(N[i])

if sum_1 == sum_2:
    print('LUCKY')
else:
    print('READY')
