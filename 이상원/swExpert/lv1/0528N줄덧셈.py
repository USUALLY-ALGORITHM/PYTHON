'''
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

10

1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1
'''

n = int(input())

odd_type = n % 2
multiple = n // 2
if odd_type == 0:
    mul = (n + 1) * multiple
    print(mul)
else:
    mul = (n + 1) * multiple
    mul += multiple + 1
    print(mul)
