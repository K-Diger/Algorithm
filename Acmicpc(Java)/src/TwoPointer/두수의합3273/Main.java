package 두수의합3273;

import java.util.*;

public class Main {

    static Scanner sc = new Scanner(System.in);

    static int n = Integer.parseInt(sc.nextLine());

    static ArrayList<Integer> array = new ArrayList<>(n);

    static int start = 0;

    static int end = n - 1;

    static int count = 0;


    /**
     * 
     * @param array : 오름차순 정렬되어있음
     * @param start : 첫 재귀 시작 인덱스 (0)
     * @param end : 처음 재귀 마지막 인덱스 (리스트의 크기 - 1) 
     * @param targetNumber : 맞추고자하는 숫자
     * @param count : targetNumber와 일치하는 숫자 쌍 갯수
     * @return count 리턴
     */
    public static int sumTwoPointer(ArrayList<Integer> array, int start, int end, int targetNumber, int count) {

        // start 인덱스가 오른쪽 포인터를 침범하면, 더 이상 쌍이 없음 리턴
        if (start >= end) {
            return count;
        }

        // 왼쪽(start) + 오른쪽(end) 가 타겟 숫자랑 같으면
        // 카운트 올리고,
        // 왼쪽 우측으로 한칸 옮기고,
        // 오른쪽 좌측으로 한칸 옮기기
        if (array.get(start) + array.get(end) == targetNumber) {
            count++;
            start++;
            end--;
        }
        // 두 수의 합이 타겟 숫자와 다른데,
        else if (array.get(start) + array.get(end) != targetNumber) {
            // 두 수의 합이 타겟 숫자보다 작으면, 왼쪽 포인터 우측으로 한칸 옮기기 --> 합을 증가하고자하는
            if (array.get(start) + array.get(end) < targetNumber) {
                start ++;
            }
            // 두 수의 합이 타겟 숫자보다 크면, 오른쪽 포인터 좌측으로 한칸 옮기기 --> 합을 줄이고자하는
            else if (array.get(start) + array.get(end) > targetNumber) {
                end --;
            }
        }
        return sumTwoPointer(array, start, end, targetNumber, count);
    }

    public static void main(String[] args) {

        for (int i = 0; i < n; i++) {
            array.add(Integer.parseInt(sc.next()));
        }

        Collections.sort(array);

        int targetNumber = Integer.parseInt(sc.next());

        count += sumTwoPointer(array, start, end, targetNumber, count);
        System.out.println(count);
    }
}