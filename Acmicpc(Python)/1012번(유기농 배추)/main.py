####### 런타임 에러 방지 코드 복붙###
import sys

sys.setrecursionlimit(10000)
####### 런타임 에러 방지 코드 복붙###
t = int(input())

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if field[x][y] == 1:
        field[x][y] = 0
        for z in range(4):
            dfs(x+dx[z], y+dy[z])
        return True
    return False


for _ in range(t):
    n, m, k = map(int, input().split()) # n = column, m = row
    field = [[0] * n for _ in range(m)]
    cnt = int(0)

    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1

    for i in range(m):
        for j in range(n):
            if field[i][j] == 1: # 배추가 있으면, 상하좌우에 배추가 더 있는지
                dfs(i, j)
                cnt += 1

    print(cnt)