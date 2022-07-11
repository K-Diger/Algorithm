# 방법 1.

# 시작시간 기준 오름차순 정렬하고,

# 시작시간 + 끝나는 시간 텀이 가장 짧고 안겹치는 애들로만 result에 담기

# 방법 2.

# 시작시간 기준, 끝나는 시간 기준 두번 정렬하고나서

# 앞선회의의 끝나는시간이 다음회의의 시작시간보다 크면 count - 1

# 0 6
# 1 4
# 2 13
# 3 5
# 3 8
# 5 7
# 5 9
# 6 10
# 8 11
# 8 12
# 12 14

# 1 4
# 5 7
# 8 11
# 12 14


import sys

input = sys.stdin.readline

n = int(input())
meeting = list()
cnt = n

# 입력
for i in range(n):
    meeting.append(input().split())

# int로 형변환
for item in meeting:
    item[0] = int(item[0])
    item[1] = int(item[1])

# 시작시간 Sort
meeting.sort(key=lambda x: x[0])

# 종료시간 Sort
meeting.sort(key=lambda x: x[1])

end = meeting[0][1]
for i in range(1, n):
    if meeting[i][0] < end:
        cnt -= 1
    else:
        end = meeting[i][1]

print(cnt)