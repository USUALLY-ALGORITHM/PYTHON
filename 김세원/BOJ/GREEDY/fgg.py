n = int(input())
arr =[]

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, name))
  

arr.sort(key=lambda a: (a[0]))

for a in arr:
    print(a[0], a[1])