package Level1.나머지1이되는수찾기;

public class Main {

    public static int solution(int n) {

        for (int i = 1; i < n; i++) {
            if (n % i == 1) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(solution(12));
    }
}
