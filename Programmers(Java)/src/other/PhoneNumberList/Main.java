package other.PhoneNumberList;

import java.util.HashMap;

class Solution {
    public boolean solution(String[] phone_book) {

        HashMap<String, String> hashPhone = new HashMap<>();

        for (String item : phone_book) {
            hashPhone.put(item, "test");
        }

        for (String item : phone_book) {
            for (int i = 0; i < item.length(); i++) {
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
