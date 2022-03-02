"""
a = 고정 비용 
b = 가변 비용 
10개 생산 1700 고정 + 70*10 

"""

a, b, c = map(int, input().split())

# > 부등식을 이용하면 편하다

if b >= c:  # 가변비용이 노트북 가격보다 같거나 크면
    print(-1)
else:
    print(a // (c - b) + 1)
