"""
수 3개를 이용해 연도를 나타냄
지구 태양 달을 나타냄
지구 E 태양 S 달 M (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
1년 = 1 1 1
1년이 지나면 세 수는 1씩 증가한다
범위를 넘어가면 1이 된다 

1 16 16

1 2 3

"""

e, s, m = map(int, input().split())


def minus(x, y, z):
    """1씩 빼기

    Args:
        x (int): e
        y (int): s
        z (int): m
    """
    return x - 1, y - 1, z - 1


year = 0
while True:
    e, s, m = minus(e, s, m)
    if e == 0:
        e = 15
    if s == 0:
        s = 28
    if m == 0:
        m = 19
    year += 1
    if (e == 1 and s == 1) and m == 1:
        print(year + 1)
        break
print(5265 // 15)
