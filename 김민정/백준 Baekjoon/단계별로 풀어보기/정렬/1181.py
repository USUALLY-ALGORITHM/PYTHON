# 단어 정렬 (https://www.acmicpc.net/problem/1181)

N = int(input())
word_list = []

for i in range(N):
    word = str(input())
    word_list.append((word, len(word)))

word_list = list(set(word_list))
word_list.sort(key=lambda x:(x[1], x[0]))

for word in word_list:
    print(word[0])