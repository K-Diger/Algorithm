# 배열 관련 메모

---

# 배열 정렬하기

    Arrays.sort(nToStringArray);

---

# 정수 자료형 자릿수 단위로 슬라이싱해서 문자열 배열만들기

### Main.java

    long n = 123l;

    String[] nToStringArray = String.valueOf(n).split("");

    for (String s : nToStringArray) {
        System.out.println("s = " + s);
    }

### 출력결과 

s = 1

s = 2

s = 3

---

