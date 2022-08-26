package Level1.같은숫자는싫어;


import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public int[] solution(int [] arr) {

        // ArrayList 로 답안을 가공하기 위함
        ArrayList<Integer> answer = new ArrayList<>(arr.length);
        int currentSearchValue = 1000001;


        // 제일 중요한 부분
        // 1. 입력받은 배열을 순회한다.
        // 2. 순회하는 원소가 currentSearchValue 와 다르면? (말 그대로 접한 적 없는 원소이기 때문)
        // 3. answer List 에 넣는다.
        // 4. currentSearchValue 를 현재 순회중인 원소로 변경한다. (다음 반복문 기준으로 이전의 원소값과 비교할 것이기 때문이다.)
        for (int item : arr) {
            if (item != currentSearchValue) {
                answer.add(item);
                currentSearchValue = item;
            }
        }

        // 최종 답을 담을 int 배열
        int[] finalAnswer = new int[answer.size()];

        // for 문 동작 중 length 함수를 계속 호출하는 것을 방지하기 위해
        int finalAnswerLength = finalAnswer.length;
        
        for (int i = 0; i < finalAnswerLength; i++) {
            finalAnswer[i] = answer.get(i);
        }

        return finalAnswer;
    }

    public static void main(String[] args) {
        int [] arr = {1, 1, 3, 3, 0, 1, 1};

        Main main = new Main();

        System.out.println(Arrays.toString(main.solution(arr)));
    }
}
