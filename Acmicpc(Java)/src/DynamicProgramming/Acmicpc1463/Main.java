package DynamicProgramming.Acmicpc1463;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(br.readLine());
        int [] dp = new int[x+3];

        dp[0] = 0;
        dp[1] = 0;
        dp[2] = 1;

        for (int i = 3; i <= x; i++) {

            //dp 배열에는 각 수에 대한 최소 카운트가 들어가 있음
            dp[i] = dp[i-1] + 1;

            //3으로 나누어 떨어질 때 비교 -> 현재 최소 카운트 VS 인덱스를 3으로 나눈 후의 카운트 +1(나눌때의 카운트 증가)
            if (i % 3 == 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1);

            //2으로 나누어 떨어질 때 비교 -> 현재 최소 카운트 VS 인덱스를 2로 나눈 후의 카운트 +1(나눌때의 카운트 증가)
            if (i % 2 == 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1);
            
        }

        System.out.println(dp[x]);
    }
}