# 상수 (https://www.acmicpc.net/problem/2908)

A, B = map(list, input().split())

A = int(A[2]) * 100 + int(A[1]) * 10 + int(A[0])
B = int(B[2]) * 100 + int(B[1]) * 10 + int(B[0])

print(max(A, B))

"""
a, b = map(str, input().split())

a = list(reversed(a))
b = list(reversed(b))

a = a[0] + a[1] + a[2]
b = b[0] + b[1] + b[2]

print(max(a, b))
"""

"""
A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)
"""