package Level1.행렬의덧셈220827;

public class Main {

    public static int[][] solution(int[][] arr1, int[][] arr2) {
        int [][] answer = new int [2][2];

        answer[0][0] = arr1[0][0] + arr2[0][0];
        answer[0][1] = arr1[0][1] + arr2[0][1];
        answer[1][0] = arr1[1][0] + arr2[1][0];
        answer[1][1] = arr1[1][1] + arr2[1][1];

        return answer;
    }

    public static void main(String[] args) {

        int [][] arr1 = {{1, 2}, {2, 3}};
        int [][] arr2 = {{3, 4}, {5, 6}};

        System.out.println(solution(arr1, arr2));

    }
}
