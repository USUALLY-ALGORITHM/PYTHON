a = input().split('-')

res = 0
for i in a[0].split('+'):
    res += int(i)
for i in a[1:]:
    for j in i.split('+'):
        res -= int(j)

print(res)
