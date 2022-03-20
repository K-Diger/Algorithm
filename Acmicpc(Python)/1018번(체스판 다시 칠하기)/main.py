n, m = map(int, input().split())
board = [input() for i in range(n)]
cnt = int(0)

for j in range(n):
    for k in range(m-1):
        print(j, "행", k, "열:", board[j][k], "   ", j, "행", k+1, "열:",  board[j][k+1])
        if board[j][k] == board[j][k+1] and board[j][k] == 'B':
            k = 0
            cnt += 1
            board[j][k+1] = 'W'

        elif board[j][k] == board[j][k+1] and board[j][k] = 'W':
            k = 0
            cnt += 1
            board[j][k + 1] = "B"

print(cnt)