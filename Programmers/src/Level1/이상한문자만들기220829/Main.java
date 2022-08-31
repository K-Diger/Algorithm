package Level1.이상한문자만들기220829;

import java.util.StringTokenizer;

public class Main {

    public static String solution(String s) {

        String[] StringToArray = new String[s.length()];
        String answer = "";

        for (int i = 0; i < StringToArray.length; i++) {
            if (i % 2 == 0) {
                answer += StringToArray[i];
            }
        }

        return answer;
    }

    public static void main(String[] args) {

        System.out.println(solution("next TT hihi"));
    }
}
