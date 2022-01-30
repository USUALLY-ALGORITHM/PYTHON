n = int(input())

cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
						# 시각을 문자열로 바꾼 후 '3'이 포함되었는지 확인
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
                
print(cnt)
