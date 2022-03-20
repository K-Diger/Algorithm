####### 런타임 에러 방지 코드 복붙###
import sys

sys.setrecursionlimit(10000)
####### 런타임 에러 방지 코드 복붙###

n = int(input())
graph = [[0] * n] * n
vertex = graph

for i in range(n):
    vertex[i] = input().split()

def dfs(j, k):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    if j < 0 or j >= n or k < 0 or j >= n:
        return False

    if vertex[j][k] == 1:
        graph[j][k] = 1
        dfs(k, j)
    else:
        for z in range(4):
            dfs(j+dx[z], k+dy[z])

for j in range(n):
    for k in range(n):
        if vertex[j][k] == 1:
            dfs(j, k)

print(graph)