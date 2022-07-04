import sys

input = sys.stdin.readline

n = int(input())

target = list()
stack = list()
popped_list = list()

answer = list()

for i in range(1, n+1):
    target.append(int(input()))
    stack.append(i)

for i in range(len(target)):
    if stack.pop() ==

print(target)
print(stack)