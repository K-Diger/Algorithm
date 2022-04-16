package Acmicpc1260;

import java.io.IOException;
import java.util.Stack;

public class Main {

    
    //n = 정점갯수
    //m = 간선갯수
    //v = 다음 정점 번호
	static void dfs(int[][] arr, int n, int m, int v) throws IOException {
        Stack<Integer> stack = new Stack<>();

        //현재 방문중인 노드
        int current = v;
        
        //이미 방분했던 노드
        boolean[] visited = new boolean[n + 1];
        
        //시작점
        stack.push(0);
        stack.push(current);

        //스택이 비어있지 않으면 반복
        while (stack.peek() != 0) {

            //다음 탐색 노드는 최대값으로
            int next = Integer.MAX_VALUE;

            //간선 갯수만큼 반복
            for (int i = 0; i < m; i++) {
                //현재 방문중인 노드가 그래프에 있는 것이라면
                if (current == arr[i][0]) {
                    //그래프에는 있지만 방문 처리가 안된것이라면
                    if (!visited[arr[i][1]]) {
                        //
                        next = Math.min(next, arr[i][1]);
                    }
                }
            }
        }
    }
}
