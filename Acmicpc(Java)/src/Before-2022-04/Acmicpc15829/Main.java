package Acmicpc15829;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {

        //서로소 인 수 1
        int r = 31;

        //서로소 인 수 2
        int m = 1234567891;

        // (a_i % m * r^i % m) = Hash
        // (a_i * r^i) % m = Hash

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long l = Integer.parseInt(br.readLine());

        String target = br.readLine();

        long result = 0;

        for (int i = 0; i < l; i++) {
            long rr = (int) Math.pow(r, i);
            int a = target.charAt(i) - 'a' + 1;
            result += (long) (a % m) *(rr%m);
        }

        System.out.println(result);
    }
}