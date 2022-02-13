"""
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 
프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.
https://www.acmicpc.net/problem/1157

Mississipi
"""


n = str(input())

n_lower = n.lower()
n_set = list(set(n_lower))
max_cnt = 0
max_alpha = ""
for i in n_set:
    if max_cnt < n_lower.count(i):
        max_cnt = n_lower.count(i)
        max_alpha = i
    elif max_cnt == n_lower.count(i):
        max_alpha = "?"
print(max_alpha.upper())
