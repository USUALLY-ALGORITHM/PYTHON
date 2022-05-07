E, S, M = map(int, input().split())
e, s, m = 1, 1, 1

cnt = 0

while True:
    cnt += 1
    if E == e and S == s and M == m :
        break
    e += 1
    s += 1
    m += 1
    
    if e == 16 :
        e = 1
    if s == 29 :
        s = 1
    if m == 20 :
        m = 1
        
print(cnt)
