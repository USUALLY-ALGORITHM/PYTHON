# 다이얼 (https://www.acmicpc.net/problem/5622)

dial = list(input())
alph = ['ABC', 'DEF', 'GHI', 'JKL','MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0
for i in dial:
    for j in alph:
        if i in j:
            time += alph.index(j) + 3
print(time)

"""
num_dict = {'ABC':3, 'DEF':4, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
word = list(input(())
result = []

for i in num_dict.keys():
    for j in word:
        if j in i:
            result.append(num_dict[i])
        else:
            pass
print(sum(result))
"""