"""
정수 N 입력 
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 경우의 수를 출력한다 

5
"""

# H 입력
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 3이 포함되어 있으면 카운트 증가
            if "3" in str(i) + str(j) + str(k):
                count += 1
print(count)
