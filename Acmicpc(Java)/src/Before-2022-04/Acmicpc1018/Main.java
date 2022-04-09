package Acmicpc1018;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int cnt = 0;

        String [] board = new String[n];

        for (int i = 0; i < n; i++) {
            board[i] = sc.nextLine();
        }

        for (int j = 0; j < n - 1; j++) {
            if (board[j].substring(j + 1, j + 2).equals(board[j].substring(j, j+1))) {
                cnt += 1;
            }
        }

        System.out.println(cnt);
    }
}
