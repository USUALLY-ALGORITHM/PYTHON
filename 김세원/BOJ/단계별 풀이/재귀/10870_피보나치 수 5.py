def sol(n):
    if n <= 1:
        return n

    return sol(n-1)+sol(n-2)

n = int(input())
print(sol(n))
