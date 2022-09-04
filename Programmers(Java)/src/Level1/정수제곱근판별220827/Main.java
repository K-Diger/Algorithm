package Level1.정수제곱근판별220827;

public class Main {

    // n 이 어떤 수 x 의 제곱이면
    // x + 1 의 제곱을 출력하기
    public static long solution(long n) {

        long answer = 0L;

        // 입력 받은 수의 제곱근 구하기
        double doubleSqrt = Math.sqrt(n);

        // 입력 받은 수의 제곱근의 소수점만 받아오기
        double modSqrt = doubleSqrt - (int) doubleSqrt;

        // 제곱근의 소수점이 남아 있으면 -1 리턴
        if (modSqrt > 0) {
            answer = -1L;
        } else if (modSqrt == 0) {
             answer = (long) Math.pow(doubleSqrt + 1, 2);
//            answer = (long) ((long) (doubleSqrt + 1) * (doubleSqrt + 1));
        }
        return answer;
    }
    public static void main(String[] args) {
        solution(3);
    }
}
