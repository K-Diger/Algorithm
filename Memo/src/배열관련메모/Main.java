package 배열관련메모;

public class Main {

    public static void main(String[] args) {

        long n = 123l;

        String[] nToStringArray = String.valueOf(n).split("");

        for (String s : nToStringArray) {
            System.out.println("s = " + s);
        }
    }
}
