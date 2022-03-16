import sys
from collections import Counter

n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(int(sys.stdin.readline()))

print(round(sum(data)/n))

data.sort()
print(data[n//2])

tmp = Counter(data).most_common()

if len(tmp) > 1:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])

print(max(data)-min(data))
