package String.src.YoSeoPooS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        List<Integer> circle = new ArrayList<>();
        List<Integer> answer = new ArrayList<>();

        for (int i = 1; i < n + 1; i++) {
            circle.add(i);
        }

        int adding = k;

        while (answer.size() != circle.size()) {

            answer.add(circle.get(k-1));
            k += adding;

            if (k > circle.size() - 1) {
            }

            System.out.println(answer);

        }

    }
}
