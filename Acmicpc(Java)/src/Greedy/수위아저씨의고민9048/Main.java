package 수위아저씨의고민9048;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < t; i++) {
            int row = Integer.parseInt(sc.next());
            int column = Integer.parseInt(sc.next());
            int lighting = Integer.parseInt(sc.next());

            boolean [][] office = new boolean[row][column];

            for (int j = 0; j < lighting; j++) {
                int lightRow = Integer.parseInt(sc.next());
                int lightColumn = Integer.parseInt(sc.next());

                office[lightRow - 1][lightColumn - 1] = true;
            }

            System.out.println(Arrays.deepToString(office));
            System.out.println(calcLightOff(office, row, column));
        }
    }

    public static int calcLightOff(boolean[][] office, int row, int column) {
        int cnt = 0;

        int middleOfficeValue = column / 2;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (office[i][j] == true && j <= middleOfficeValue) {
                    cnt += (i + j) + j;
                    office[i][j] = false;
                } else if (office[i][j] == true && j > middleOfficeValue) {

                }
            }
        }

        return cnt;
    }
}
