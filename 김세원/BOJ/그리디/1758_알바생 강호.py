n = int(input())
tip = []
result = 0

for _ in range(n):
    tip.append(int(input()))

tip.sort(reverse=True)

for i in range(n):
    if tip[i] - ((i+1)-1) >= 0: #나는 바보다 .. 결국 그냥 i만 빼주면 됨..
        result += tip[i] - ((i+1)-1)
    else:
        break

print(result)
