import sys

n = int(sys.stdin.readline())
count = [0] * 10001 # 입력 받은 숫자가 몇개가 나왔는지 세는 카운트 리스트

for _ in range(n):
    count[int(sys.stdin.readline())] += 1 # 카운트 리스트에 입력받은 수의 갯수 만큼 넣어준다

for i in range(10001):
    if count[i] > 0: # count 리스트 i번째에 있는게 한 번이상 나왔으면
        for j in range(count[i]): # 나온 횟수만큼 반복해서
            print(i) # 해당하는 숫자를 출력