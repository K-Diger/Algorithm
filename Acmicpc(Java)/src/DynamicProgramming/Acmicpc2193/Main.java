package DynamicProgramming.Acmicpc2193;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {


        long dp[] = new long[100];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        dp[1] = 1; //1
        dp[2] = 1; //10
        dp[3] = 2; //100, 101




//        dp[4] = 3; //1000, 1010, 1001
//        dp[5] = 5; //10000, 10100, 10101, 10010, 10001
//        dp[6] = 8; //100000, 100001, 101010, 100010, 101000, 100100, 100101

        for (int i = 4; i < 100; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        System.out.println(dp[n]);
    }
}
