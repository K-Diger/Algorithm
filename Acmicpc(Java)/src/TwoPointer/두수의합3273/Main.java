package 두수의합3237;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static Scanner sc = new Scanner(System.in);

    static int n = Integer.parseInt(sc.nextLine());

    static ArrayList<Integer> array = new ArrayList<>(n);

    static int start = 0;

    static int end = n - 1;

    static int count = 0;


    public static void main(String[] args) {

        for (int i = 0; i < n; i++) {
            array.add(Integer.parseInt(sc.next()));
        }

        int targetNumber = Integer.parseInt(sc.next());

        while (true) {

            // 아래 모든 조건을 돌다가 start 와 end 가 같아지는 시기가 오면 반복문 종료
            if (start == end) {
                break;
            }

            // 왼쪽(start) + 오른쪽(end) 가 타겟 숫자랑 같으면
            // 카운트 올리고,
            // 왼쪽 한칸 옮기고,
            // 오른쪽 초기화 하고 다시 수행
            if (array.get(start) + array.get(end) == targetNumber) {
                count ++;
                start ++;
                end = n - 1;
            }
            else if (array.get(start) + array.get(end) != targetNumber) {
                end --;
                // end 가 start 바로 앞까지 왔는데도 두 수의 합이 타겟과 다르다면
                // start 한칸 옮기고
                // end 초기화
                if (end == start + 1) {
                    start ++;
                    end = n - 1;
                }
            }
        }
        System.out.println(count);
    }
}
