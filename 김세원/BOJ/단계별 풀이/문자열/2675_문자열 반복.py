n = int(input())

for i in range(n):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) *i
    print(text)
