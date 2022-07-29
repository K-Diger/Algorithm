import sys

input = sys.stdin.readline

n, m = map(int, input().split())

sst = []
visited = [False] * (n + 1)


def dfs():
    # 문제에서 요구하는, m길이의 숫자가 완성되면 dfs 종료
    if len(sst) == m:
        print(' '.join(map(str, sst)))
        return

    # i : 1 부터 n 까지
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        sst.append(i)

        # 가지치기를 위해 dfs 재 호출
        dfs()

        # # DFS 와의 큰 차이점 --> 이전에 확인한 것을 빼버림
        # sst.pop()
        # visited[i] = False

dfs()