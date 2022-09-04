# 입출력 관련 메모

---

# 더 빠르게 입력받기 (BufferedReader)

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

---

# 더 빠르게 입력받기 Advanced. BufferedReader 와 StringTokenizer

    // BufferedReader
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // StringTokenizer
    StringTokenizer st = new StringTokenizer(" ");

    // BufferedReader + StringTokenizer -> BufferedReader 로 입력받은 후 StringTokenizer 로 문자열 분리
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

---

# 문자열 더 빠르게 슬라이싱하기 (StringTokenizer.nextToken())

> 문자열을 자르게 위해 split을 사용할땐, **split은 정규식을 기반**으로 자르는 로직으로서 내부는 복잡하다.
>
> 그에 비해 **StringTokenizer**의 **nextToken() 메소드**는 **단순히 공백 자리를 땡겨 채우는 것**이다.
>
> 정규식 처리가 딱히 필요한게 아닌 경우 StringTokenizer가 효율적이다.


    // BufferedReader + StringTokenizer -> BufferedReader 로 입력받은 후 StringTokenizer 로 문자열 분리
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    st.nextToken();
    st.nextToken();
    st.nextToken();
    st.nextToken();
    st.nextToken();
    ...