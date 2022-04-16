n = input()

length = range(ord('A'), ord('Z')+1)
arr = {}
for i, val in enumerate(length):
    arr[val] = i+1

for i in n:
    print(arr[ord(i)], end=' ')
