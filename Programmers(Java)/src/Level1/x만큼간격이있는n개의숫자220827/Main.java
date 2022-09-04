package Level1.x만큼간격이있는n개의숫자220827;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static long[] solution(int x, int n) {
        long [] answer = new long [n];
        answer[0] = x;

        for (int i = 1; i < n; i++) {
            answer[i] += answer[i-1] + x;
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] inputValue = br.readLine().split(" ");

        int x = Integer.parseInt(inputValue[0]);
        int n = Integer.parseInt(inputValue[1]);

        System.out.println(solution(x, n));
    }
}
