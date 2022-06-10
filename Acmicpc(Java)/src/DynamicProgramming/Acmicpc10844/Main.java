package DynamicProgramming.Acmicpc10844;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


//n = 1
//	1 2 3 4 5 6 6 7 8 9
//
//	9
//
//n = 2
//	12 23 34 45 56 67 78 89
//	21 32 43 54 65 76 87 98
//	10
//
//	17
//
//n = 3
//	123 234 345 456 567 678 789
//	987 876 765 654 543 432 321 210
//	121 232 343 454 565 676 787 898
//	101 212 323 434 545 656 767 878 989
//
//	32
//
//n = 4
//	1234 2345 3456 4567 5678 6789
//	9876 8765 7654 6543 5432 4321 3210
//
//	1232 2343 3454 4565 5676 6787 7898
//	8987 7876 6765 5654 4543 3432 2321
//
//	1212 2323 3434 4545 5656 6767 7878 8989
//
//	9898 8787 7676 6565 5454 4343 3232 2121 1010
//
//	1210 2321 3432 4543 5654 6765 7876 8987
//	+ 7
//
//	52


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[100+1];

        dp[0] = 9;
        dp[1] = 17;
        dp[2] = 32;

        for (int i = 3; i < dp.length; i++) {

            dp[i] = (dp[i-1] + (n*5))%1000000000;
        }
        System.out.println(dp[n-1]);
    }
}
