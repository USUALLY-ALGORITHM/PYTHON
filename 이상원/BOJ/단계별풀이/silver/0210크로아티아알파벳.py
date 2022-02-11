"""
https://www.acmicpc.net/problem/2941
"""
alpha = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
n = str(input())

cnt = 0

for i in alpha:
    if i in n:
        n = n.replace(i, "?")

print(len(n))
