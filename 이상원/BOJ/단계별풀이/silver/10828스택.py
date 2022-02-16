# FIXME: 시간 초과

n = int(input())
result = []

for i in range(n):
    command = list(map(str, input().split()))
    length = len(result)
    if command[0] == "push":
        result.append(command[1])
    elif command[0] == "pop":
        res = print(result.pop()) if length != 0 else print(-1)
    elif command[0] == "size":
        print(len(result))
    elif command[0] == "empty":
        length = 1 if length == 0 else 0
        print(length)
    elif command[0] == "top":
        res = result[-1] if length != 0 else -1
        print(res)
