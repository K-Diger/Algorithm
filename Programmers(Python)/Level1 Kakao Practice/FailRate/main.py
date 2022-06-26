# 실패율이 높은 스테이지부터 내림차순으로

# 멈춰있는 스테이지가 젤 많은거

#

def solution(n, stages):
    fail_rate = {}
    sub = len(stages)

    for item in range(1, n + 1):
        print(sub)
        if sub != 0:
            fail_rate[item] = stages.count(item) / sub
            sub -= stages.count(item)
        else:
            fail_rate[item] = 0

    print(fail_rate)

    return sorted(fail_rate, key=lambda abc: fail_rate[abc], reverse=True)


# n = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]

n = 4
stages = [4, 4, 4, 4, 4]
print(solution(n, stages))
