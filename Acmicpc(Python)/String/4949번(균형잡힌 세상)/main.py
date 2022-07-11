# 입력 문자열에서,
# ( 갯수랑 ) 갯수 비교
# [ 갯수랑 ] 갯수 비교
# 후 다르면 no
# 같으면 yes
# --> 오답, 다른방향으로 바라보고 있는 괄호가 있으면 갯수가 같아도 다르게됨 ==> )( 같은 꼴


import sys

input = sys.stdin.readline

while True:
    string = input().rstrip()
    stack = []

    if string == ".":
        break

    for item in string:
        # 왼쪽 대-소 괄호
        if item == '[' or item == '(':
            stack.append(item)

        # 오른쪽 대괄호 일때 -> 스택 안에 [ 가 있는지 검사
        elif item == ']':
            # [ 가 있으면
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        # 오른쪽 소괄호
        elif item == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
