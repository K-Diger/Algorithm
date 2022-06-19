# 스택을 구현할 때 필요한 메서드

# 1. 스택 생성
# 2. 스택 크기 반환
# 3. 스택 원소를 문자욜로 변환
# 4. Push
# 5. Pop
# 6. Peek
# 7. Clear
# 8. IsEmpty
# 9. IsFull
# 10. Size

from collections import deque

deque = deque()

deque.append("Test Data")
deque.appendleft("Test Data Insertion At LeftSide")
deque.pop()
deque.popleft()
deque.clear()
deque.copy()
deque.count("해당 값과 일치하는 원소의 개수를 계산")

class Stack:

    # 스택 생성
    # limit 은 최대 스택의 크기를 담은 변수
    def __init__(self, limit: int):
        self.top = []
        self.limit = limit

    # 스택 크기 반환
    # -> bool : 타입 힌트로,
    def __len__(self) -> bool:
        return len(self.top)

    # 스택 내용 문자열 타입으로 변환
    def __str__(self) -> str:
        return str(self.top[::1])

    def push(self, item):
        if len(self.pop()) >= self.limit:
            self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack Underflow")
            exit()

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

        else:
            print("underflow")
            exit()

    def isEmpty(self) -> bool:
        return len(self.top) == 0

    #스택을 비움
    def clear(self):
        self.top=[]

    #스택 안에 특정 item이 포함되어 있는지를 bool값으로 반환
    def isContain(self, item) -> bool:
        return item in self.top

    #스택이 비어있는 지를 bool값으로 반환
    def isEmpty(self) -> bool :
        return len(self.top)==0

    #스택이 가득 차 있는 지를 bool값으로 반환
    def isFull(self) -> bool :
        return self.size()==self.limit

    #스택의 크기를 int 값으로 반환
    def size(self) -> int :
        return len(self.top)




