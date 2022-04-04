# 셀프 넘버 (https://www.acmicpc.net/problem/4673)

def self_num(n):
    result = n
    for i in str(n):
        result += int(i)
    return result

num = []
for i in range(1, 10001):
    num.append(self_num(i))

for i in range(1, 10001):
    if i in num:
        pass
    else:
        print(i)

"""
num = set(range(1, 10001)) # 전체 자연수
generated_num = set() # 생성자를 담을 변수

for a in range(1, 10001) :
    for b in str(a):
        a += int(b)
    generated_num.add(a)

self_num = num - generated_num

for i in sorted(self_num) :
    print(i)
"""