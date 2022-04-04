"""
동빈이는 두개 배열 a, b 있음 
n개의 원소로 이뤄짐 모두 자연수 
k번의 바꿔치기 연산 수행 
a에 있는 원소 하나와 b의 원소 하나를 골라 바꾸는것 
a의 원소의 합이 최대 

5 3
1 2 5 4 3
5 5 6 6 5

"""


def mySol():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = sorted(a)
    b = sorted(b, reverse=True)

    for i in range(k):
        # a가 b보다 작은 경우를 생각해줘야 함 !!!
        a[i], b[i] = b[i], a[i]

    print(sum(a))


def bookSol():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    print(sum(a))
