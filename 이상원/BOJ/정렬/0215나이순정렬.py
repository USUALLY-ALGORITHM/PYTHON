"""
가입한 사람의 나이와 이름이 가입한 순서로 주어짐 
나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬
"""

n = int(input())

usrInfo = []
for i in range(n):
    age, name = map(str, input().split())
    usrInfo.append((age, name, i))

answer = sorted(usrInfo, key=lambda x: (x[0], x[2]))
for person in answer:
    print(f"{person[0]} {person[1]}")
