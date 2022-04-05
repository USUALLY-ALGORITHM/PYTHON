# 크로아티아 알파벳 (https://www.acmicpc.net/problem/2941)

text = input()
alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alph:
    if i in text:
        text = text.replace(i, '*')
print(len(text))
