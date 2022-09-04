package Level1.하샤드수220827;

public class Main {

    
    // 하샤드 수 : x 의 자릿수의 합으로 x가 나누어 떨어져야함
    public static boolean solution(int x) {
        int xLength = String.valueOf(x).length();
        int num = 0;

        for (int i = 1; i < xLength + 1; i++) {
            num += Integer.parseInt(String.valueOf(x).substring(i-1, i));
        }
        return x % num == 0;
    }

    public static void main(String[] args) {
        solution(1234);
    }
}
