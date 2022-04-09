//package Acmicpc1010;
//
//import java.io.BufferedInputStream;
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//
//public class Main {
//
//    static int [][] dp = new int[30][30];
//
//    public static int combination(int n, int m){
//
//        if (n == m || m == 1) { return 1; }
//
//
//        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < m; j++) {
//                dp[i][j] = combination(n);
//            }
//        }
//    }
//
//
//
//    public static void main(String[] args) throws IOException {
//
//        // nCr 조합 공식을 이용해야한다.
//
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int t = br.read();
//        int n, m;
//
//        combination(n, m);
//    }
//}
