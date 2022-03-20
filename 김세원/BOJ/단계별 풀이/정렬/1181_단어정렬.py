n = int(input())
data = []

for i in range(n):
    word = str(input())
    data.append((word, len(word)))

data = list(set(data))
data.sort(key=lambda x:(x[1],x[0]))

for word in data:
    print(word[0])


