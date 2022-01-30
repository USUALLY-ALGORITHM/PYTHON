"""
0과 1로 이뤄진 문자열 s 
s에 있는 모든 숫자를 전부 같게 하고 싶다 
s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것 -> 0을 1로 1을 0으로

0001100
"""

s = str(input())
split0 = list(filter(None, s.split("0")))
split1 = list(filter(None, s.split("1")))

lengh0 = len(split1) # 2
lengh1 = len(split0) # 1

if lengh0 > lengh1:
    print(lengh1)
elif lengh0 < lengh1:
    print(lengh0)
else:
    print(lengh0)
