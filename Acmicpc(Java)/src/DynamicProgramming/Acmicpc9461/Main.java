package DynamicProgramming.Acmicpc9461;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static long[] dp = new long[101];

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        long[] answerList = new long[t];

        padovanArray();

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());

            answerList[i] = dp[n-1];
        }

        for (int j = 0; j < t; j++) {
            System.out.println(answerList[j]);
        }
    }




    static void padovanArray() {
        dp[0] = 1L;
        dp[1] = 1L;
        dp[2] = 1L;
        dp[3] = 2L;

        for (int i = 4; i < 100; i++) {
            dp[i] = dp[i - 2] + dp[i - 3];
        }
    }

}
