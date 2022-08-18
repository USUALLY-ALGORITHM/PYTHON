for tc in range(10):
    N = int(input())
    lst = list(map(str, input()))
    stck = list()

    left = ['(', '{', '[', '<']
    right = [')', '}', ']', '>']
    
    for i in range(N):
        if lst[i] in left:
            stck.append(lst[i])
        if lst[i] in right:
            if right.index(lst[i]) == left.index(stck[-1]):
                stck.pop()
            else:
                break

    res = 0
    if len(stck) == 0:
        res = 1

    print("#{} {}".format(tc + 1, res))
