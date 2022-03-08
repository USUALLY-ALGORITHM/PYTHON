"""
재귀적 패턴으로 별을 찍어보자 
N이 3의 거듭제곱 3 9 27 ... 이라고 할때 N의 패턴은 NxN정사각 모양
가운데를 제외한 나머지 칸에 별이 있다 
***
* *
***

"""


def star(n, x):
    out = []
    if n == 3:
        return x
    else:
        for i in x:
            out.append(i*3)
        for i in x:
            out.append(i+' ' * len(x)+i)
        for i in x:
            out.append(i*3)
        return star(n//3, out)


if __name__ == '__main__':
    n = int(input())
    first = ['***', '* *', '***']
    final = star(n, first)
    for i in final:
        print(i)
