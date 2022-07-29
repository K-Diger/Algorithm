import sys

input = sys.stdin.readline

test_case = int(input())

stair = [int(input()) for _ in range(test_case)]

dp = [0] * test_case


def dynamic_programming(test_case, stair, dp):
    # 입력 원소가 1개일때
    if test_case == 1:
        return stair[0]

    # 입력 원소가 2개일 때
    elif test_case == 2:
        return stair[0] + stair[1]

    # 입력 원소 3개일 때
    elif test_case == 3:
        return max(stair[0] + stair[1] + stair[3], stair[0] + stair[2], stair[3])

    # 입력 원소 4개 이상일 때
    elif test_case > 3:
        
        # 첫번째 계단
        dp[0] = stair[0]

        # 첫번째 계단 + 두번째 계단
        dp[1] = stair[0] + stair[1]

        # (첫번째 계단 + 두번째 계단 + 네번째 계단) vs (첫번째 계단 + 세번째 계단 + 네번째 계단)
        dp[2] = max(stair[0] + stair[1] + stair[3], stair[0] + stair[2], stair[3])

    # 3칸 연속으로 오르지 않는 예외를 어떻게 처리할까용

    for i in range(3, test_case):
        dp[i] = dp[i - 1] + max(stair[i + 1], stair[i + 2])

        if i + 2 == test_case - 1:
            break

    remove_target = {0}

    dp = [i for i in dp if i not in remove_target]

    return dp[-1]


print(dynamic_programming(test_case, stair, dp))
