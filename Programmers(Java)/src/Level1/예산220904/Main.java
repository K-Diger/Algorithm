package Level1.예산220904;

import java.util.Arrays;

public class Main {

    public static int solution(int[] d, int budget) {

        int dLength = d.length;
        Arrays.sort(d);
        int count = 0;

        for (int i = 0; i < dLength; i++) {
            if (budget - d[i] >= 0) {
                budget -= d[i];
                count ++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
//        System.out.println(solution(new int[]{1, 3, 2, 5, 4}, 9));
        System.out.println(solution(new int[]{2, 2, 3, 3}, 10));
    }
}
