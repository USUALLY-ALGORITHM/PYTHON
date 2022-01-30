data = input()
cnt0 = 0 # 전부 0으로 바꾸는 경우
cnt1 = 0 # 전부 1로 바꾸는 경우

if data[0] == '1':
    cnt0 += 1
else:
    cnt1 += 1
    
# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
				# 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            cnt0 += 1
				# 다음 수에서 0으로 바뀌는 경우
        else:
            cnt1 += 1
            
print(min(cnt0, cnt1))
