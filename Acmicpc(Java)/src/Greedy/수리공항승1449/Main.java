package 수리공항승1449;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double n = Integer.parseInt(sc.next());
        double l = Integer.parseInt(sc.next());

        ArrayList<Integer> flood = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            flood.add(Integer.parseInt(sc.next()));
        }
        Collections.sort(flood);

        System.out.print(taping(flood, n, l));
    }

    public static int taping(ArrayList<Integer> flood, double n, double l) {

        for (int i = 0; i < n; i++) {
            double coverRangeMin = flood.get(i) - 0.5;
            double coverRangeMax = flood.get(i) + 0.5;

        }

    }
}


class Solution {
    public boolean solution(String s) {
        if (s.length() == 4 || s.length() == 6) {
            for (int i = 0; i < s.length(); i ++) {
                if (Character.isDigit(s.charAt(i))) {
                    return true;
                }
            }
        }

        return false;
    }
}