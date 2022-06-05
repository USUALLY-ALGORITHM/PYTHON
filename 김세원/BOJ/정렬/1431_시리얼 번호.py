# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append(input())
#
# arr.sort(key=lambda a:(len(a),sum(int(x) for x in a if x.isnumeric())))
#
# for i in arr:
#     print(i)
# push 를 위한


n = int(input())

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

arr = []
for i in range(n):
    a = input()
    arr.append(a)

arr.sort(key = lambda x:(len(x), sum_num(x), x))
for i in arr:
    print(i)
