package Level1.부족한금액계산하기220904;

public class Main {

    public static long solution(int price, int money, int count) {
        long totalPrice = 0l;

        // 탑승 횟수만큼 곱한 값을 누적합 시킨다.
        for (int i = 1; i < count + 1; i++) {
            totalPrice += i * price;
        }

        // 누적합 한 금액이 현재 가진돈 보다 많으면
        // 누적합 금액 - 현재 금액
        if (totalPrice > money) {
            return totalPrice - money;
        }

        // 누적합 금액과 현재 금액이 같거나
        // 누적합 금액이 현재 금액보다 작으면
        // --> 돈이 모자라지 않은 상황
        // 0 리턴
        return 0l;
    }

    public static void main(String[] args) {
        System.out.println(solution(3, 20, 4));
    }
}
