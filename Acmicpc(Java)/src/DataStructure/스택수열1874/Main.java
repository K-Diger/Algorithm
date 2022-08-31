package 스택수열1874;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        int [] target = new int[n];

        int [] customStack = new int[n];

        for (int i = 0; i < n; i++) {
            target[i] = Integer.parseInt(sc.nextLine());

            for (int j = 0; j < target[i]; j++) {
                customStack[i] += 1;
            }
        }

    }
}
