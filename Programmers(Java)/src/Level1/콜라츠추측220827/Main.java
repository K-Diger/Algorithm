package Level1.콜라츠추측220827;

public class Main {

    // 오버플로우 발생을 막아야함!
    // 왜냐? 최대 7999999 * 3 + 1 --> 반복하다보면 int 범위 벗어나게 되어있음

    public static int solution(int num) {

        long longNumber = num;

        int count = 0;

        if (longNumber == 1) return 0;

        while (longNumber != 1) {

            if (longNumber % 2 == 0) {
                longNumber /= 2;
                count ++;
            }
            else if (longNumber % 2 != 0) {
                longNumber = (longNumber * 3) + 1;
                count ++;
            }

            if (count >= 500) {
                return -1;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        System.out.println(solution(626331));
    }
}
