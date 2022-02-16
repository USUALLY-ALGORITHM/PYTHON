"""
하나의 수열에 다양한 수 존재 
크기에 상관없이 나열됨
큰수 부터 작은수 내림차순 

3
15
27
12

"""

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

sortedList = sorted(arr, reverse=True)
for i in sortedList:
    print(i, end=" ")
