sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

def solution(sizes):

    width = int(0)
    height = int(0)

    width_idx = int(0)

    for i in range(len(sizes)):
        if sizes[i][0] > width:
            width = sizes[i][0]
            width_idx = i
        if sizes[i][1] > height:
            height = sizes[i][1]

        if sizes[width_idx][0] < sizes[i][0] and sizes[width_idx][1] > sizes[i][1]:
            height = sizes[i][1]
    return width*height

print(solution(sizes))