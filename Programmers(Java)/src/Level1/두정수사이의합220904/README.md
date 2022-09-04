# 두 정수 사이의 합

## 문제 설명

두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.

예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

## 제한 조건

a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.

a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.

a와 b의 대소관계는 정해져있지 않습니다.

## 입출력 예

|a| b| 	return|
|---|---|---|
|3| 	5| 	12|
|3| 	3| 	3|
|5| 	3| 	12|

---

# 풀이 - 코드

    public class Main {
    
        public static long solution(int a, int b) {
    
            long biggerNumber = whichNumberIsBigger(a, b);
            long smallerNumber = whichNumberIsSmaller(a, b);
    
            long answer = 0l;
    
            for (long i = smallerNumber; i < biggerNumber + 1; i++) {
                answer += i;
            }
    
            return answer;
        }
    
        public static int whichNumberIsBigger(int a, int b) {
            if (a > b) {
                return a;
            } else if (a < b) {
                return b;
            }
            return a;
        }
    
        public static int whichNumberIsSmaller(int a, int b) {
            if (a > b) {
                return b;
            } else if (a < b) {
                return a;
            }
            return a;
        }
    
    
        public static void main(String[] args) {
            System.out.println(solution(5, 3));
        }
    }

---

# 풀이 - 상세

### whichNumberIsBigger

    public static int whichNumberIsBigger(int a, int b) {
        if (a > b) {
            return a;
        }
        else if (a < b) {
            return b;
        }
        return a;
    }

a, b 중 어떤 수가 더 큰지 반환하는 메서드이다.


### whichNumberIsSmaller
    public static int whichNumberIsSmaller(int a, int b) {
        if (a > b) {
            return b;
        }
        else if (a < b) {
            return a;
        }
        return a;
    }

a, b 중 어떤 수가 더 작은지 반환하는 메서드이다.

### for-loop

    long answer = 0l;
    
    for (long i = smallerNumber; i < biggerNumber + 1; i++) {
        answer += i;
    }

위 두개의 메서드로부터 알아낸, 작은 수 ~ 큰 수 범위의 수를 반복문을 통해 누적합한다.