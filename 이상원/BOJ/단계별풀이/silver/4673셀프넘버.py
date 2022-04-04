"""
셀프 넘버는 양의 정수 n에 대해 d(N)을 n과 n의 각 자리수를 더하는 함수로 가정
d(75) = 75+7+5 = 87

"""


def d(n):
    for i in str(n):
        n += int(i)
    return n


not_self = []
for i in range(1, 10000):
    not_self.append(d(i))

for i in range(1, 10001):
    if i in not_self:
        continue
    else:
        print(i)
        
