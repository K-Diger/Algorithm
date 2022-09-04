package Level1.이상한문자만들기220829재도전;

import java.util.StringTokenizer;

public class Main {

    public static String solution(String s) {

        StringTokenizer stringTokenSpitedSpace = new StringTokenizer(s, "");
        StringBuilder stringBuilder = new StringBuilder();

        while (stringTokenSpitedSpace.hasMoreTokens()) {
            String tempNextToken = stringTokenSpitedSpace.nextToken();
            int tempStringLength = tempNextToken.length();

            for (int i = 0; i < tempStringLength; i++) {
                if (tempNextToken.charAt(i) == ' ') {
                    stringBuilder.append(" ");
                }
                // 인덱스가 짝수일 때
                else if (i == 0 || i % 2 == 0) {
                    stringBuilder.append(Character.toUpperCase(tempNextToken.charAt(i)));
                }
                // 인덱스가 홀수일 때
                else if (i % 2 == 1) {
                    stringBuilder.append(tempNextToken.charAt(i));
                }
            }
        }

        return stringBuilder.substring(0, stringBuilder.length());
    }

    public static void main(String[] args) {

        System.out.println(solution("try hello world"));
        System.out.println(solution("  a  b cd"));
        System.out.println(solution("A  B"));
    }
}
