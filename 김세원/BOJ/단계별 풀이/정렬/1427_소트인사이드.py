n=int(input())
data = []

for i in str(n):
    data.append(int(i))

data.sort(reverse=True)

for i in data:
    print(i,end='')