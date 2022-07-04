rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

board = [[column for column in range(1, columns + 1)] for row in range(rows)]

t = board[0][columns-1] + 1

print(board)

for row in range(1, rows):
    for col in range(columns):
        board[row][col] = t

        t += 1


for x1, y1, x2, y2 in queries:
    temp = board[x1 - 1][y1 - 1]

    min_value = temp

    for k in range(x1 - 1, x2 - 1):
        for_loop_min_value = board[k + 1][y1 - 1]
        board[k][y1 - 1] = for_loop_min_value
        min_value = min(min_value, for_loop_min_value)


