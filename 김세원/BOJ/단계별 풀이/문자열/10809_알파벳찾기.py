n = str(input())
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in n:
        print(n.index(i), end =' ')
    else:
        print(-1, end = ' ')
