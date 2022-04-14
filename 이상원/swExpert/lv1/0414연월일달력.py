'''

5
22220228
20150002
01010101
20140230
11111111

'''
maxMonth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
n = int(input())
arr = []
for i in range(n):
    inputDate = input()
    year = inputDate[:4]
    month = inputDate[4:6]
    date = inputDate[6:]
    if int(month) == 0 or int(date) == 0 or int(month) > 12:
        arr.append(-1)
        continue
    elif int(month) == 2 and int(date) > 28:
        arr.append(-1)
        continue

    arr.append(f'{year}/{month}/{date}')

for i in range(len(arr)):
    print(f'#{i+1} {arr[i]}')
