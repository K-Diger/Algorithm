package Level1.직사각형별찍기220827;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String [] inputContent = br.readLine().split(" ");

        int n = Integer.parseInt(inputContent[0]);
        int m = Integer.parseInt(inputContent[1]);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // System.out.print("*");
                sb.append("*");
            }
            // System.out.println();
            sb.append("\n");
        }
        System.out.print(sb);
    }
}
