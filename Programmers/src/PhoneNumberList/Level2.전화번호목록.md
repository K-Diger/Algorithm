> 문제 설명
>
> 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
> 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
>
>        구조대 : 119
>        박준영 : 97 674 223
>        지영석 : 11 9552 4421
>
>        전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
>        어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

>        제한 사항
>
>        phone_book의 길이는 1 이상 1,000,000 이하입니다.
>        각 전화번호의 길이는 1 이상 20 이하입니다.
>        같은 전화번호가 중복해서 들어있지 않습니다.

>        입출력 예제
>        phone_book 	return
>        ["119", "97674223", "1195524421"] 	false
>        ["123","456","789"] 	true
>        ["12","123","1235","567","88"] 	false

>        입출력 예 설명
>
>        입출력 예 #1
>        앞에서 설명한 예와 같습니다.

>        입출력 예 #2
>        한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

>        입출력 예 #3
>        첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.


    package PhoneNumberList;
    
    import java.util.HashMap;
    
    class Solution {
        public boolean solution(String[] phone_book) {
        
                HashMap<String, String> hashPhone = new HashMap<>();
                
                // 해시맵에 phone_book 원소를 하나씩 담는다. 이 때 value 값은 아무거나 넣어도 상관없다.
                for (String item : phone_book) {
                    hashPhone.put(item, "test");
                }
        
                // phone_book 원소를 하나씩 순회한다.
                for (String item : phone_book) {
                    // phone_book 의 원소의 문자열 길이만큼 반복한다.
                    for (int i = 0; i < item.length(); i++) {
                        // 해시맵에 들어있는 Key값과 문자열 최대길이까지 반복자를 하나씩 늘려가면서 원소를 substring 한 문자열과 비교한다. 
                        // 이때 Key 값과 문자열을 자른 것과 같은 것이 있으면
                        // false, 즉 접두사 전화번호가 존재하는 것이다.

                        // ex)
                        // item = "119"
                        // hashPhone = {"119", "test"}
                        // if -> hashPhone 에 null이라는 key를 가진게 있나 ?
                        // if -> hashPhone 에 1이라는 key를 가진게 있나??
                        // if -> hashPhone 에 11 이라는 Key를 가진게 있나?
                                -> 조건문 false

                        // item = "1195524421"
                        // hashPhone = {"119" = "test", "1195524421" = "test}
                        // if -> hashPhone 에 1이라는 key를 가진게 있나 ?
                        // if -> hashPhone 에 11이라는 key를 가진게 있나??
                        // if -> hashPhone 에 119 이라는 Key를 가진게 있나?
                                -> 조건문 true

                        if (hashPhone.containsKey(item.substring(0, i))) {
                            return false;
                        }
                    }
                }
        
                return true;
            }
    }
    
    
    public class Main {
        public static void main(String[] args) {
        
                String [] phone_book = {"119", "97674223", "1195524421"};
        //        String [] phone_book = {"123","456","789"};
        //        String [] phone_book = {"12","123","1235","567","88"};
        
        
                Solution s = new Solution();
        
        
                System.out.println(s.solution(phone_book));
        
            }
    }