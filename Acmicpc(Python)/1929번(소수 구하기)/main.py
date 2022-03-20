m, n = map(int, input().split())

# 2를 제외한 2의배수
# 3을 제외한 3의배수
# 5를 제외한 5의배수
# 7을 제외한 7의배수

def m_to_n_prime(m, n):
    prime = [2, ]
    for i in range(m, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i - 1:
                prime.append(i)
    return prime

res = m_to_n_prime(m, n)

for i in range(len(res)):
    print(res[i])