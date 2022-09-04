# 문자열 관련 메모

---

# 특정 문자열 반복하기

### String.repeat()

    // 문자열 반복
    // Level 1. 핸드폰번호가리기 에서 사용됨
    public class StringRepeat {
    
        public static void main(String[] args) {
            String phoneNumber = "01012345678";
            int maskingLength = phoneNumber.length() - 4;
    
            phoneNumber = "*".repeat(maskingLength) + phoneNumber.substring(maskingLength);
    
            System.out.println(phoneNumber);
        }
    }

---
# 문자열을 자주 변경해야하는 경우 

### StringBuilder

    StringBuilder stringBuilder = new StringBuilder();

    // 문자열 사이즈 반환 (일반적으로 실제 문자열보다 더 크게 잡하져있음)
    stringBuilder.capacity();

    // 문자열 자체의 길이 (일반적으로 실제 문자열보다 더 크게 잡하져있음)
    stringBuilder.length();

    // 문자열 추가
    stringBuilder.append();

    // 문자열 삭제 (인덱스시작점, 인덱스끝점) 시작 <= 범위 < 끝
    stringBuilder.delete();

    // 문자열 삭제 (특정 인덱스)
    stringBuidler.deleteCharAt();

    // 문자열 삽입 (특정 인덱스)
    stringBuidler.insert();


    // --------------------- //
    // String 과 동일만 메서드 //


    // 문자 조회 (특정 인덱스에 대한 문자 반환)
    stringBuidler.charAt()

    // 문자열 검색 (해당하는 문자열에 대한 위치(시작 위치) 반환)
    stringBuidler.indexOf()
    
    // 문자열 검색 (해당하는 문자열에 대한 위치(끝나는 위치) 반환)
    stringBuidler.lastIndexOf()
    
    // 문자열 길이
    stringBuidler.length()
    
    // 문자열 교체
    stringBuidler.replace()
    
    // 문자열 자르기
    stringBuidler.substring()
    
    // 문자열 타입캐스팅
    stringBuidler.toString()