from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

friends_list = [list(input().strip()) for _ in range(n)]



def bfs(start, graph):
    queue = deque([start])
    visited = [[False] * n] * n
    count = [0] * n

    while queue:
        depth = int(1)
        current = queue.popleft()
        print(queue)

        for i in range(len(graph)):
            # Depth 가 1, 2 인 건너 친구들 까지만 친구로 포함 해야 한다.
            if depth > 2:
                break
            for j in range(len(graph)):
                if not visited[i][j] and graph[i][j] == 'Y':
                    queue.append(graph[i])
                    visited[i][j] = True
                    depth += 1
                    count[i] += 1
    print(count)



bfs(friends_list[0], friends_list)