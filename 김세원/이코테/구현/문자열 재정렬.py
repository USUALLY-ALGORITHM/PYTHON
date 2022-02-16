data = input()
answer = []
num = 0

# 문자를 하나씩 확인
for x in data:
		# 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        answer.append(x)
		# 숫자는 따로 더하기
    else:
        num += int(x)

# 알파벳을 오름차순으로 정렬
answer.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if num != 0:
    answer.append(str(num))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(answer))
