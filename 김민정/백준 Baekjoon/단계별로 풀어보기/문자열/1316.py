# 그룹 단어 체커 (https://www.acmicpc.net/problem/1316

N = int(input())

for i in range(N):
    word = input()
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j+1:]:
            N -= 1
            break
print(N)

"""
cnt = 0
n = int(input())

for i in range(n):
    word = input()
    cnt += list(word) == sorted(word, key=word.find) # ex) word가 aabcca일때 sorted(word, key=word.find)는 ['a', 'a', 'a', 'b', 'c', 'c']가 된다. 같지 않으므로 그룹 단어가 아님을 알 수 있다.

print(cnt)
"""