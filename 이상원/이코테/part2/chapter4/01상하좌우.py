"""
5
R R R U D D
"""


def solution() -> str:
    N = int(input())
    route = list(map(str, input().split()))
    xy = [1, 1]

    route_dict = {"L": [0, -1], "R": [0, 1], "D": [1, 0], "U": [-1, 0]}

    for i in route:
        xy[0] += route_dict[i][0]
        xy[1] += route_dict[i][1]
        if xy[0] == 0:
            xy[0] += 1
        elif xy[1] == 0:
            xy[1] += 1

    return xy


if __name__ == "__main__":
    print(solution())
