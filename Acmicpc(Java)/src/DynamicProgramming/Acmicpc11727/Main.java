package DynamicProgramming.Acmicpc11727;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int [] dp = new int[1000];

        //2x1 일때의 경우의 수
        dp[0] = 1;

        //2x2 일때의 경우의 수
        dp[1] = 3;

        //2x3 일때의 경우의 수
        dp[2] = 5;


        //점화식 : 구하고자 하는 수 = 이전 경우의 수 + (그 이전 경우의 수 *2)
        for (int i = 3; i < n; i++) {
            dp[i] = (dp[i-1] + dp[i-2]*2) % 10007;
        }

        System.out.println(dp[n-1]);
    }
}
