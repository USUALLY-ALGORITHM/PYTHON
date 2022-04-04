# 시험 성적 (https://www.acmicpc.net/problem/9498)

grade = int(input())

if 90 <= grade <= 100:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')