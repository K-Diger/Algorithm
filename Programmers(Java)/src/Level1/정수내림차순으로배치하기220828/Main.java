package Level1.정수내림차순으로배치하기220828;

import java.util.Arrays;

public class Main {

    // Long.parseLong() 으로 String -> Long 변환
    
    public static long solution(long n) {

        String[] nToStringArray = String.valueOf(n).split("");

        int iterSize = nToStringArray.length - 1;

        Arrays.sort(nToStringArray);

        StringBuilder sbAnswer = new StringBuilder();

        for (int i = iterSize; i >= 0; i--) {
            System.out.println(nToStringArray[i]);
            sbAnswer.append(nToStringArray[i]);
        }

        return Long.parseLong(sbAnswer.toString());
    }


    public static void main(String[] args) {
        long n = 118372L;

        System.out.println(solution(n));

    }
}
