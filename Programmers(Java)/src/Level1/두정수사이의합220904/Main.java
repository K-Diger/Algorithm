package Level1.두정수사이의합220904;

public class Main {

    public static long solution(int a, int b) {

        long biggerNumber = whichNumberIsBigger(a, b);
        long smallerNumber = whichNumberIsSmaller(a, b);

        long answer = 0l;

        for (long i = smallerNumber; i < biggerNumber + 1; i++) {
            answer += i;
        }

        return answer;

    }

    public static int whichNumberIsBigger(int a, int b) {
        if (a > b) {
            return a;
        } else if (a < b) {
            return b;
        }
        return a;
    }

    public static int whichNumberIsSmaller(int a, int b) {
        if (a > b) {
            return b;
        } else if (a < b) {
            return a;
        }
        return a;
    }


    public static void main(String[] args) {

        System.out.println(solution(5, 3));

    }
}
