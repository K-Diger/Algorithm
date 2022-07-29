n = int(input())


def custom_sum(n):
    if n == 1:
        return 1

    return n + custom_sum(n - 1)


print(custom_sum(n))
