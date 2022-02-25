def solution(s):
    s_len = len(s)
    answer = [''] * (s_len // 2)
    for i in range(s_len // 2):
        base = s[:i + 1] # 기준 문자열
        count = 1
        for j in range(i + 1, s_len, i + 1):
            new = s[j:i + j + 1] # 기준 뒤 문자열
            if base == new:
                count += 1
            else:
                if count != 1:
                    answer[i] += str(count)
                answer[i] += base
                count = 1
                base = new
        if count != 1:
            answer[i] += str(count)
        answer[i] += base

        s_len = min(len(answer[i]), s_len)

    return s_len

# 1. 문자열을 자르는 단위마다 결과를 array에 저장해주고, 결과로 나온 문자열의 길이를 비교해주기
# 2. 첫 번째 for 문에서는 기준 문자열을 base 변수에 넣어주었다. 문자열이 몇 번 반복되었는지 확인하기 위해 count 변수를 선언한다.
# 3. 두 번째 for 문에서는 그 다음 문자열을 new 변수에 넣어주었다.
# 3-1. base와 new가 같다면 기준 문자열은 변하지 않으며 count에 1을 더해준다. 다음 반복문에서 new를 그 다음 문자열로 업데이트해주어 다시 base와 비교한다.
# 3-2. base와 new가 다르다면 base를 결과 문자열에 더해주었다. (count가 1이 아닌 경우 count도 더해준다). new를 기준 문자열로 삼기 위해 base를 new로 업데이트해주고 count를 1로 초기화한다. 다음 반복문에서 new를 그 다음 문자열로 업데이트해주어 다시 base와 비교한다.
# 4. 두 번째 for문을 다 돌고 나온 결과 문자열의 길이를 비교하여 더 작은 길이로 업데이트해준다.