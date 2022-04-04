n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0

a.sort() ## a의 수 재배열

for i in range(n):
    s += a[i] * b.pop(b.index(max(b)))
 ## b는 재배열할 수 없으므로 팝을 이용해서 최대값 선출
    
print(s)
