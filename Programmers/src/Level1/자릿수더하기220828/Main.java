package Level1.자릿수더하기220828;

import java.util.*;

public class Main {

    public static int solution(int n) {
        String [] nToString = String.valueOf(n).split("");
        int iterSize = nToString.length;
        int answer = 0;

        for (int i = 0; i < iterSize; i++) {
            answer += Integer.parseInt(nToString[i]);
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(456));
    }
}
