import sys
from collections import deque


input = sys.stdin.readline

t = int(input())


# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

def bfs(start, cnt):

    # queue 에는 방문 예정인 노드를 담고 있다.
    queue = deque([start])

    visited[start] = True

    while queue:
        # 현재 방문중인 노드 = 방문 대기중인 큐에서 꺼내기
        visiting_node = queue.popleft()

        if visited.count(True) == n:
            return cnt

        # print("graph = ", graph)

        # item 에는, 현재 방문중인 노드가 연결된 노드의 번호를 가지고 있다.
        for item in graph[visiting_node]:
            # print("visiting_node = ", visiting_node)
            # print("graph[visiting_node] = ", graph[visiting_node])
            # print("item = ", item)
            # 그 item이, 방문 처리가 되지 않은 것이라면
            if not visited[item]:
                # 방문 처리를 해주고
                visited[item] = True
                # 그 노드를 다음 방문할 큐에 넣는다
                queue.append(item)

                cnt += 1

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (1 + n)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(1, 0))

