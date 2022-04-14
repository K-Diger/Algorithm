package DynamicProgramming.Acmicpc1912;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        //dp 배열
        int [] dp = new int[100000];
        int [] arr = new int[100000];

        //입력 값 - n 입력받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());


        //입력 값 - 배열 입력받기
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dp[0] = arr[0];
        int max = arr[0];

        for (int i = 1; i < n; i++) {

            // dp[i] 에는
            // (현재 인덱스 바로 이전까지의 합의 결과 + 현재 인덱스의 배열 값) VS (현재 인덱스의 배열 값)
            dp[i] = Math.max(dp[i-1] + arr[i], arr[i]);

            //현재 최대값과, 새롭게 구한 최댓값 중에서 최댓값 갱신
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);
    }
}