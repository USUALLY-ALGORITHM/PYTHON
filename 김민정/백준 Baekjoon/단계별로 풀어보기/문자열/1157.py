# 문자열 반복 (https://www.acmicpc.net/problem/1157)

word = input().upper()
word_list = list(set(word))
max_count = []

for i in word_list:
    max_count.append(word.count(i))

if max_count.count(max(max_count)) > 1:
    print("?")
else:
    print(word_list[(max_count.index(max(max_count)))])