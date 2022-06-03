n = int(input())
result = n

for i in range(0,n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result -= 1
            break
            
print(result)
