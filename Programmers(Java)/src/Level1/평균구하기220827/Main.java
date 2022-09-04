package Level1.평균구하기220827;

public class Main {

    public static double solution(int[] arr) {
        int arrayLength = arr.length;
        double answer = 0;

        for (int i = 0; i < arrayLength; i++) {
            answer += arr[i];
        }

        return answer / arrayLength;
    }
}
