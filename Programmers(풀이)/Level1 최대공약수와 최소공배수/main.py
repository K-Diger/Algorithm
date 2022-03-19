n, m = int(120), int(480)

def solution(n, m):
    gcd = int(0) #최대 공약수
    lcm = int(0) #최소 공배수

    if n > m:
        n, m = m, n

    if (m % n == 0):
        # 두 수를 나눴을때 나머지가 0이면 두 수중 작은 수가 최대 공약수
        gcd = n
    else:
        # 두 수를 나눴을때 나머지가 홀수이면 두 수를 나눈 나머지가 최대공약수
        gcd = 1

    if (gcd == n): #최대공약수가 n이면 최소공배수는 m
        lcm = m
    else:
        lcm = n*m

    answer = [gcd, lcm]
    return answer

print(solution(n, m))
