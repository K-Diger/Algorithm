package Level1.두개뽑아서더하기220904;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static int[] solution(int[] numbers) {
        Map<Integer, Integer> tempHashMapForCombination = new HashMap<>();
        int numbersLength = numbers.length;

        for (int i = 0; i < numbersLength - 1; i++) {
            for (int j = i + 1; j < numbersLength; j++) {
                tempHashMapForCombination.put(numbers[i] + numbers[j], 0);
            }
        }

        return tempHashMapForCombination.keySet().stream()
                .sorted()
                .mapToInt(i -> i)
                .toArray();
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{2, 1, 3, 4, 1})));
    }
}
