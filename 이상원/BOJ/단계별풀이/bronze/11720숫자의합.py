"""
N개의 숫자가 공백 없이 
숫자를 모두 더해라 

"""
n = int(input())
nums = str(input())
res = 0
for i in nums:
    res += int(i)

print(res)
