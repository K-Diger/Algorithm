from collections import deque
import sys

input = sys.stdin.readline

test_case = int(input())


def dfs(start, target, graph):
    visited = []
    stack = [graph[start]]
    count = int(0)

    while stack:
        current = stack.pop()

        if current == target:
            return count + 1

        # 한번도 지목 당하지 않은 사람의 경우
        # 방문 처리
        # 그 사람이 가리키는 다음 사람 스택에 넣기
        elif current not in visited:
            visited.append(current)
            stack.append(graph[current])
            count += 1
        else:
            return 0


for i in range(test_case):
    person_num = int(input())
    graph = [0]
    for j in range(person_num):
        graph.append(int(input()))

    if person_num not in graph:
        print(0)

    else:
        print(dfs(1, person_num, graph))
