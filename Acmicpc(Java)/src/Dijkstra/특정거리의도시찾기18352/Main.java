package 특정거리의도시찾기18352;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

    // 입력 모듈
    static Scanner sc = new Scanner(System.in);
    // 노드 갯수
    static int N = Integer.parseInt(sc.next());
    // 간선 갯수
    static int L = Integer.parseInt(sc.next());
    // 타겟 비용
    static int K = Integer.parseInt(sc.next());
    // 출발 노드 번호
    static int X = Integer.parseInt(sc.next());
    // 인접 그래프
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>(L);

    public static void main(String[] args) {
        
        // 그래프 초기화 (간선 갯수만큼 반복하여 각각 인접 노드를 담을 리스트를 할당해준다.)
        for (int i = 0; i < N; i++) {
            graph.add(new ArrayList<>());
        }

        // 그래프 셋팅 (간선 갯수만큼 반복하여 실제 그래프의 인접 노드가 무엇이 있는지 입력받아 담는다.)
        for (int j = 0; j < N; j++) {
            graph.get(Integer.parseInt(sc.next())).add(Integer.parseInt(sc.next()));
        }


    }

}