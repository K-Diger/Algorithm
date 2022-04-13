package DynamicProgramming.Acmicpc9095;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

//    1 -> 1 [1]
//    2 -> 1+1, 2 [2]
//    3 -> 1+1+1, 1+2, 2+1, 3 [4]
//    4 -> 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1 [7]


//    5 -> 1+4, 2+3, 3+2 = 7+4+2 = 13
//    6 -> 1+5, 2+4, 3+3, 4+2 = 13 + 7 + 4 + 2 = 26
//    7 -> 1+6, 2+5, 3+4, 4+3, 5+2 = 26 + 13 + 7 +

    public static void main(String[] args) throws IOException {

        int[] dp = new int[12];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int t = 0;

        for (int i = 0; i < n; i++) {
            t = Integer.parseInt(br.readLine());

            for (int j = 4; j <= t; j++) {
                dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
            }

            System.out.println(dp[t]);
        }

    }
}
