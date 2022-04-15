def fac(n):
    result = 1

    if n == 0:
        return 1

    if n > 0:
        result = n * fac(n-1)
    return result

n = int(input())
print(fac(n))
