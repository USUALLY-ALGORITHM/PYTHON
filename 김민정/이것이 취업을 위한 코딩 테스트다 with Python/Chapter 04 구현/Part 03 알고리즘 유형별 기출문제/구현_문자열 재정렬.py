S = input()
ar = list()
num = list()
num_sum = 0

for i in S:
    if i.isalpha():
        ar.append(i)
    else:
        num.append(i)

ar.sort()
for i in num:
    num_sum += int(i)

ar.append(num_sum)
for i in ar:
    print(i, end='')
