package DynamicProgramming.Acmicpc2011;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int [] dp = new int[5000];

        String num = (br.readLine());

        int n = num.length();

        dp[0] = 1;
        dp[1] = 2;
        dp[2] = 3;

        for (int i = 3; i < n; i++) {
            dp[i] = ((dp[i-1]*dp[i-2]) - (dp[i-2]*dp[i-3]))%1000000;
            System.out.println(dp[i]);
        }

        System.out.println(dp[n-1]);
    }
}
