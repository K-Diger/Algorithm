package Level1.자연수뒤집어배열로만들기220828;

public class Main {

    // 자릿수연산이 필요하면, String 배열로 쪼개서 가공하기
    
    public static int[] solution(long n) {

        String[] longToStringArray = String.valueOf(n).split("");
        int iterSize = longToStringArray.length - 1;

        int [] answer = new int[iterSize + 1];
        int j = 0;

        for (int i = iterSize; i >= 0; i --) {
            answer[j] = Integer.parseInt(longToStringArray[i]);
            j ++;
        }

        return answer;
    }

    public static void main(String[] args) {

        System.out.println(solution(12345));

    }
}
