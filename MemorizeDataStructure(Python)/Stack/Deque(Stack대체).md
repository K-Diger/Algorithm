# Python 에서 Stack 을 간편하게 사용하기

---

## collections Library's Deque

![Deque](https://mblogthumb-phinf.pstatic.net/MjAxOTA0MThfMjcx/MDAxNTU1NTMxOTk3NjM1.5AEXPRQeNYX8dxSzgTCiATI-xprr8WIQY52DVXk91_gg.lgVBOfBws5gg9nYlLEuotRHLLQv-exifkTNPxdb06YUg.PNG.sooftware/anod.png?type=w800)

그림과 같이, 좌측과 우측 으로 데이터를 삽입-삭제가 가능하다.

Deque 는 Double-Ended-Queue 를 의미한다.

---

    from collections import deque
    
    deque = deque()
    
    deque.append("Test Data")
    deque.appendleft("Test Data Insertion At LeftSide")
    deque.pop()
    deque.popleft()
    deque.clear()
    deque.copy()
    deque.count("해당 값과 일치하는 원소의 개수를 계산")

---

### 데이터 추가 하기
> deque.append()

### 데이터 추가 하기 (가장 좌측에 데이터 추가)
> deque.appendleft()

### 데이터 꺼내기
> deque.pop()

### 데이터 꺼내기 (가장 좌측에 데이터를 꺼낸다)
> deque.popleft()

### 특정 원소의 갯수 찾기
> deque.count(찾고 싶은 원소의 값)

### 원소 모두 삭제하기
> deque.clear()

### 원소 모두 복제하기
> deque.copy()