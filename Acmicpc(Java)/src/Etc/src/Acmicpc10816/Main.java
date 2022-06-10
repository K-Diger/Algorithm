package Acmicpc10816;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


//        입력
//
//        첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
//        둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
//        숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
//
//        셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
//        넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며,
//        이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
//
//        출력
//
//        첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

    /*

    10
    6 3 2 10 10 10 -10 -10 7 3
    8
    10 9 -5 2 3 4 5 -10

    */

public class Main {


    public static void main(String[] args) throws IOException {
        HashMap<Integer, Integer> answer = new HashMap<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

    }


//    public static void main(String[] args) throws IOException {
//
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        int n = Integer.parseInt(br.readLine());
//        int [] userList = new int[n];
//        StringTokenizer st = new StringTokenizer(br.readLine());
//
//        for (int i = 0; i < n; i++) {
//            userList[i] = Integer.parseInt(st.nextToken());
//        }
//
//        Arrays.sort(userList);
//
//        int m = Integer.parseInt(br.readLine());
//        int [] targetList = new int[m];
//        StringTokenizer str = new StringTokenizer(br.readLine());
//
//
//        for (int i = 0; i < m; i++) {
//            targetList[i] = Integer.parseInt(str.nextToken());
//        }
//
//
//        List<Integer> answer = new ArrayList<>();
//
//        for(int i = 0; i < m; i++) {
//            answer.add(binary_upper(n, userList, targetList) - binary_low(n, userList, targetList));
//        }
//
//    }
//
//    public static int binary_low(int n, int[] userList, int[] k) {
//
//        int start = 0;
//        int mid = 0;
//        int end = n - 1;
//
//        while (start <= end) {
//            mid = (start + end) / 2;
//
//            if (userList[mid] >= k) end = mid - 1;
//
//            else start = mid + 1;
//
//        }
//        return start;
//    }
//
//    public static int binary_upper(int n, int[] userList, int[] k) {
//        int start = 0;
//        int mid = 0;
//        int end = n-1;
//
//        while (start <= end) {
//            mid = (start + end) / 2;
//
//            if (userList[mid] > k) end = mid -1;
//
//            else start = mid + 1;
//        }
//        return start;
//    }

}
