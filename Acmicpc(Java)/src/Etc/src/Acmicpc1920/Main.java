package Acmicpc1920;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] array = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());


        for (int i=0; i<n; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(array);

        int m = Integer.parseInt(br.readLine());
        int[] result = new int[m];

        st = new StringTokenizer(br.readLine());

        for (int i=0; i<m; i++) {
            int num = Integer.parseInt(st.nextToken());

            int temp = binarySearch(array, num, 0, n-1);

            result[i] = temp != -1 ? 1 : 0;
        }

        for (int i=0; i<m; i++) {
            System.out.println(result[i]);
        }

    }

    static int binarySearch(int[] array, int target, int start, int end) {

        if (start > end) {
            return -1;
        }

        int mid = (start+end)/2;

        if (array[mid] == target) {
            return mid;
        } else if (array[mid] > target) {
            return binarySearch(array, target, start, mid-1);
        } else {
            return binarySearch(array, target, mid+1, end);
        }

    }
}
