'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

'''

tc = int(input())
for item in range(tc):
    num = int(input())
    arr = list(map(int, input().split()))

    arr = arr[::-1]
    maxValue = arr[0]

    profit = 0
    for i in range(len(arr)):
        if arr[i] >= maxValue:
            maxVal = arr[i]
        else:
            profit += maxVal - arr[i]

    print(f'#{item+1} {profit}')

# 마지막날 매매가를 최대로 거꾸로 오면서 해당 매매가와 비교, 새 매매가가 현재보다 크면 최대값을 매매일로 설정
# 그렇지 않으면 i번째 날 매매가 차이로 이익 계산

# arr 뒤집는 것 시간 초과 나는 것 같음
T = int(input())

# T만큼 반복
for tc in range(1, T+1):
    # 자연수 N의 개수 입력
    N = int(input())
    # N 리스트 입력
    N_list = list(map(int, input().split()))

    # N_list의 마지막 값을 최대값으로 설정
    max_value = N_list[-1]
    # 이익 변수 초기화
    profit = 0

    # N-2번째 인덱스부터 0번째 인덱스까지 1씩 감소하면서 반복 순회
    for i in range(N-2, -1, -1):
        # 만약 현재 매매가가 최대값보다 크면 최대값을 변경
        if N_list[i] >= max_value:
            max_value = N_list[i]
        # 현재 매매가가 최대값보다 크지 않으면 차익을 profit 변수에 더해준다
        else:
            profit += max_value - N_list[i]

    # 결과 출력
    print('#{} {}'.format(tc, profit))
