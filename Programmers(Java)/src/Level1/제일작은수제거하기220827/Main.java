package Level1.제일작은수제거하기220827;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static int[] solution(int[] arr) {
        int arrLength = arr.length;
        List<Integer> preList = new ArrayList<>();
        int [] answer = new int [arrLength - 1];
        int min = 99999999;
        int minIndex = 0;

        if (arrLength == 1) {
            return new int[]{-1};
        }

        // 최소값 인덱스 구하기
        for (int i = 0; i < arrLength; i++) {
            if (min > arr[i]) {
                min = arr[i];
                minIndex = i;
            }
        }

        // 최소값 인덱스로 인해 0으로 설정한 인덱스를 제외하고 리스트에 담기
        for (int i = 0; i < arrLength; i++) {
            if (i != minIndex) {
                preList.add(arr[i]);
            }
        }

        // 리스트 내용 배열로 치환
        for (int i = 0; i < arrLength - 1; i++) {
            answer[i] = preList.get(i);
        }

        return answer;
    }

    public static void main(String[] args) {

        int [] arr = {4, 3, 2, 1};
        int [] arr3 = {4, 3, 1, 2, 7, 9, 11, 0, -1, 23};

        int [] arr2 = {10};

        solution(arr);
        System.out.println();
        solution(arr3);
    }
}
