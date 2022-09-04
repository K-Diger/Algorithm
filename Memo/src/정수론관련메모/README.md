# 정수론 관련 메모

---

# 최대 공약수 (GCD)

    for (int i = 1; i <= n && i <= m; i++) {
        if (n % i == 0 && m % i == 0) {
            gcd = i;
        }
    }

i 가 1부터 시작하여

n 보다 작거나 같거나, m 보다 작거나 같으면 계속 반복

n을 i 로 나눈 나머지가 0이고, m 을 i 로 나눈 나머지가 0이면 최대공약수

---

# 최소 공배수 (LCM)

최소 공배수 = N * M / 최대공약수

---

# 제곱근

    Math.sqrt(n);

    // 제곱근의 소수점 자르기
    double doubleSqrt = Math.sqrt(n);
    double modSqrt = doubleSqrt - (int) doubleSqrt;

---

# 제곱

    Math.pow(num, 2);