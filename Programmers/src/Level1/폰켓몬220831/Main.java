package Level1.폰켓몬220831;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static int solution(int[] nums) {
        Map<Integer, Integer> pairInformation = new HashMap<Integer, Integer>();

        int selectNumber = nums.length / 2;

        for (int item : nums) {
            if (pairInformation.get(item) == null) {
                pairInformation.put(item, 1);
            }

            else if (pairInformation.get(item) >= 0) {
                pairInformation.put(item, pairInformation.get(item) + 1);
            }
        }


        int keySize = pairInformation.keySet().size();

        // HashMap Key 최댓값
        // Integer maxKey = Collections.max(map.keySet());
        
        // HashMap Key 최솟값
        // Integer minKey = Collections.min(map.keySet());

        // HashMap Value 최댓값
        // Integer maxValue = Collections.max(map.values());

        // HashMap Value 최솟값
        // Integer minValue = Collections.min(map.values());

        // Key 갯수가, 선택할 수 있는 포켓몬 수랑 크거나 같으면
        // 선택할 수 있는 최대 포켓몬 수를 반환한다.
        if (keySize >= selectNumber) {
            return selectNumber;
        }

        // Key 갯수가 선택할 수 있는 포켓몬 수보다 작으면
        // Key 의 갯수 (서로다른 포켓몬을 조합하여 선택할 수 있는 경우의 수)를 반환한다.
        return keySize;
    }

    public static void main(String[] args) {

        int[] nums = {3, 1, 2, 3};
        int[] nums2 = {3, 3, 3, 2, 2, 4};

        System.out.println(solution(nums2));

    }
}
