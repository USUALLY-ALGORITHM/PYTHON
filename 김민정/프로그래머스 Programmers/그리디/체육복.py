def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))

    for i in reserve:
        front = i - 1
        back = i + 1
        if front in lost:
            lost.remove(front)
        elif back in lost:
            lost.remove(back)

    return n - len(lost)