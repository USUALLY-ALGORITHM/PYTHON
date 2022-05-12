T = int(input())

for tc in range(1, T+1):
    Date = input()
    month = int(Date[4:6])
    day = int(Date[6:])
    if month in (1, 3, 5, 7, 8, 10, 12):
        if day <= 31:
            print(f'#{tc} {Date[:4]}/{Date[4:6]}/{Date[6:]}')
        else:
            print(f'#{tc} -1')
    elif month in (4, 6, 9, 11):
        if day <= 30:
            print(f'#{tc} {Date[:4]}/{Date[4:6]}/{Date[6:]}')
        else:
            print(f'#{tc} -1')
    elif month == 2:
        if day <= 28:
            print(f'#{tc} {Date[:4]}/{Date[4:6]}/{Date[6:]}')
        else:
            print(f'#{tc} -1')
    else:
        print(f'#{tc} -1')
