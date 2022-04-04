'''
두 사람이 볼링을 치고 있다 
서로 무게가 다른 볼링공 고르기 
볼링공은 N개가 있으며 공의 번호는 1부터 순서대로 부여된다 
같은 무게의 공이 여러개 있을 수 있지만, 서로 다른 공으로 간주
볼링공의 무게는 1부터 N까지의 자연수 형태로 존재

N=5 M=3이며 각각의 무게가 차례대로 1 3 2 3 2 일 때 ㅂ공의 번호가 차례대로 1부터 5까지 부여된다 

고를 수 있는 볼링공의 조합을 구하라 
두 사람이 공을 고르는 경우의 수는 8가지 

5 3 
1 3 2 3 2
'''


import itertools


n, m = map(int, input().split())
ball_list = list(map(int, input().split()))

comb = list(itertools.combinations(ball_list, 2))
answer = 0
for a, b in comb:
    if a == b:
        continue
    answer += 1
print(answer)

# ------------------------책 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n  # B가 선택하는 경우의 수와 곱해주기

print(result)
