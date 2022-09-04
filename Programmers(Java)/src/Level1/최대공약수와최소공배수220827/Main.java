package Level1.최대공약수와최소공배수220827;

public class Main {

    // 최대 공약수? : 서로가 가진 약수중 가장 큰 수
    
    public static int[] solution(int n, int m) {

        int [] answer = new int [2];

        int gcd = 0;
        int lcm = 0;

        for (int i = 1; i <= n && i <= m; i++) {
            if (n % i == 0 && m % i == 0) {
                gcd = i;
            }
        }
        lcm = n * m / gcd;

        answer[0] = gcd;
        answer[1] = lcm;

        return answer;
    }

    public static void main(String[] args) {

        int n = 3;
        int m = 12;

        solution(n, m);
    }
}
