import sys
n = int(sys.stdin.readline())

user = [sys.stdin.readline().split() for i in range(n)]

for i in range(n):
    user[i][0] = int(user[i][0])

user.sort(key=lambda age:age[0])


for i in range(n):
    print(user[i][0], user[i][1])