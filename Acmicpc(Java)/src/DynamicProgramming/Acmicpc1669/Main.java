package DynamicProgramming.Acmicpc1669;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int [] powArray = new int[n+1];

        int count = 0;


        for (int i = 1; i < n+1; i++) {
            powArray[i] = (int) Math.pow(i, 2);
        }

        for (int j = n; j > 0; j--) {
            if (powArray[j] < n) {
                n %= powArray[j];
                count ++;
                j ++;

                System.out.println(powArray[j]);
            }
        }

        System.out.println(count);
    }
}
