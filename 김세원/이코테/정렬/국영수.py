n = int(input())
arr = []

for i in range(n):
    name, kor, eng, math = map(str, input().split())
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    arr.append((name, kor, eng, math))
    
arr.sort(key=lambda a:(-int(a[1]),int(a[2]),-int(a[3]),a[0]))

for a in arr:
    print(a[0])
