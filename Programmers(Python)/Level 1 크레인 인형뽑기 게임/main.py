board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    bucket = []
    answer = 0

    for col in moves:
        for row in range(len(board)):
            if board[row][col - 1] != 0:
                target = board[row][col - 1]
                bucket.append(target)
                board[row][col - 1] = 0
                if len(bucket) > 0 and target == bucket[-1]:
                    bucket.pop()
                    bucket.pop()
                    answer += 2

            break
    print(answer)
    return answer


solution(board, moves)
