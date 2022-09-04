package Level1.나누어떨어지숫자배열220904;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static int[] solution(int[] arr, int divisor) {
        int arrLength = arr.length;
        // ArrayList 를 쓰는이유 -> 몇개의 원소가 나누어떨어질지 모르기 때문에
        // 고정 크기의 row 배열로 하게되면 안쓰는 공간이 나오게 될 가능성이 있기 때문이다.
        List<Integer> needToConvertToArray = new ArrayList<>();

        for (int i = 0; i < arrLength; i++) {
            // 나누어 떨어지는게 있을 때 마다 ArrayList 에 담아준다.
            if (arr[i] % divisor == 0) {
                needToConvertToArray.add(arr[i]);
            }
        }

        // 나누어 떨어지는게 하나도 없으면 -1 을 담은 배열을 반환한다.
        if (needToConvertToArray.size() == 0) {
            return new int[]{-1};
        }

        // Integer ArrayList -> int Array
        return needToConvertToArray.stream()
                .sorted()
                .mapToInt(i -> i)
                .toArray();
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{5, 9, 7, 10}, 5)));
        System.out.println(Arrays.toString(solution(new int[]{3, 2, 6}, 10)));
        System.out.println(Arrays.toString(solution(new int[]{2, 36, 1, 3}, 1)));
    }
}
