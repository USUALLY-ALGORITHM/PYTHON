"""
문자열 S 주어지고 왼쪽 부터 확인하여 x나 +연산자를 넣어 만들 수 있는 가장 큰수를 구하라 
단, +보다 x를 먼저 계산하는 일반적인 방식과 달리 
모든 연산은 순서대로이다 

02984
567
"""

s = str(input())
result = 0

for i in s:
    num_i = int(i)
    if (num_i == 0 or num_i == 1) or result == 0:
        result += num_i
    else:
        result *= num_i

print(result)
