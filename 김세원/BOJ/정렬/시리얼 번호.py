n = int(input())
arr = []

for i in range(n):
    arr.append(input())

arr.sort(key=lambda a:(len(a),sum(int(x) for x in a if x.isnumeric())))

for i in arr:
    print(i)