def test(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    k = test(n-1) + test(n-2)
    return k

print(test(5))
print(test(7))
