package InternShip.p1;

import java.util.Arrays;

class Solution {
    public int[] solution(int[] p) {

        // 요구사항 -> 선택정렬 후 각 인덱스별 이동한 횟수 출력
        int[] answer = new int[p.length];

        for (int i = 0; i < p.length - 1; i++) {

            int minIndex = i;

            for (int j = i + 1; j < p.length; j++) {

                if (p[j] < p[minIndex]) {
                    minIndex = j;
                }

                answer[i] = (minIndex - i);

            }

            swap(p, minIndex, i);
        }


        return answer;
    }

    public static int[] swap(int[] p, int i, int j) {
        int temp = p[i];
        p[i] = p[j];
        p[j] = temp;

        return p;

    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
//        int[] p = {2, 5, 3, 1, 4};
//        int[] p = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int[] p = {2, 3, 4, 5, 6, 1};

        Arrays.stream(s.solution(p)).forEach(e -> System.out.println(e));
    }
}
