"""
숫자 1을 걸려면 2초가 필요 
한 칸 옆에 있는 숫자를 하려면 1초씩 걸린다 

"""

nums = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
}
n = str(input())
n = n.lower()

result = 0
for idx, i in nums.items():
    for j in n:
        if j in i:
            result += idx + 1
print(result)