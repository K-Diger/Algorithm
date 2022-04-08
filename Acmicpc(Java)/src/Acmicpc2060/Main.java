package Acmicpc2060;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    //컴퓨터 수 0 ~ 100
    //연결된 쌍의 수
    //연결된 쌍

    //1번 컴퓨터가 걸렸을때의 감염 갯수

    // 1-2-3
    // 1-5-2
    // 1-5-6
    // 4-7

    static int[][] graph; // 그래프 배열
    static int[] visited; // 방문 배열

    public static void bfs(int start) {

        Queue<Integer> queue = new LinkedList<>();

        //감염된 컴퓨터 수
        int cnt = 0;

        //첫 번째 방문 기록
        visited[start] = 1;

        //큐에 첫 번째 원소 삽입
        queue.offer(start);

        //큐에 원소가 있으면 반복
        while (!queue.isEmpty()) {

            //제일 앞의 원소 지우고, 변수에 담기
            int x = queue.poll();

            for (int i = 1; i < graph.length; i++) {
                if (graph[x][i] == 1 && visited[i] != 1) {
                    queue.offer(i);
                    visited[i] = 1;
                    cnt ++;
                }
            }
        }
        System.out.println(cnt);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n= sc.nextInt(); // 컴퓨터의 수
        int m = sc.nextInt(); // 네트워크 상에 연결되어 있는 컴퓨터 쌍의 수 즉, 간선의 수

        //그래프 틀
        graph = new int[n + 1][n + 1];
        
        //방문 노드
        visited = new int[n + 1];

        //그래프 세부
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        bfs(1);
    }

}