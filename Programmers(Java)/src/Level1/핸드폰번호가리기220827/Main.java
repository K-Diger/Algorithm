package Level1.핸드폰번호가리기220827;

public class Main {

    public static String solution(String phoneNumber) {
        int maskingLength = phoneNumber.length() - 4;
        phoneNumber = "*".repeat(maskingLength) + phoneNumber.substring(maskingLength);
        return phoneNumber;
    }

    public static void main(String[] args) {
        String phoneNumber = "01033334444";

        System.out.println(solution(phoneNumber));
    }
}
