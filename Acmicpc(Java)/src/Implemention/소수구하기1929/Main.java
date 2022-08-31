package 소수구하기1929;

import java.util.Scanner;

public class Main {

    // 입력값의 최대 범위인 1000000 까지의 배열을 static으로 선언
    // 인덱스에 해당하는 수가 실제 정수를 가리킨다 : prime[0] == 0, prime[1] == 1 ...
    // 소수에 해당하는 숫자는 False를 가진다
    public static boolean[] prime = new boolean[1000000];

    public static void Eratosthenes(int start, int end) {

        // 정수 0과 1은 소수가 아니므로 true 를 할당한다.
        prime[0] = prime[1] = true;

        // 정수 2부터 순회한다. (해당 숫자의 제곱에 해당하는 수 까지만 순회를 하면된다.)
        for (int i = 2; i * i <= end; i++) {

            // 현재 순회하고 있는 정수가 false 즉, 소수면
            if (prime[i] == false) {
                
                // 해당하는 정수의 제곱 수 부터 문제에서 요구하는 숫자의 범위까지 순회하여
                // 소수가 아님을 나타내준다.
                for (int j = i * i; j <= end; j += i){
                    prime[j] = true;
                }
            }
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int start = Integer.parseInt((sc.next()));
        int end = Integer.parseInt(sc.next());

        Eratosthenes(start, end);

        // 소수 출력
        for (int i = 1; i <= end; i++) {
            if (!prime[i] && i >= start) {
                System.out.println(i);
            }
        }
    }
}
