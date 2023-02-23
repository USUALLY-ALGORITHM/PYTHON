n = int(input())
m = []
result = 0

for _ in range(n):
    m.append(int(input()))

m.sort(reverse=True)

#for i in range(n):
    #if (i+1)%3 == 0:
        #result += m[i]
# print(sum(m)-result) 로 출력

for i in range(n):
    if i % 3 != 2:
        result += m[i]

print(result)
