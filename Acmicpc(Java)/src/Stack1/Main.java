package Stack1;

import java.util.ArrayList;
import java.util.Scanner;

//10828번(스택)

public class Main {


    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        Stack stack = new Stack();

        int N = in.nextInt();

        for(int i = 0; i < N; i++) {

            String str = in.next();

            switch (str) {
                case "push":
                    stack.push(in.nextInt());
                    break;
                case "pop":
                    sb.append(stack.pop()).append('\n');
                    break;
                case "size":
                    sb.append(stack.size()).append('\n');
                    break;
                case "empty":
                    sb.append(stack.empty()).append('\n');
                    break;
                case "top":
                    sb.append(stack.top()).append('\n');
                    break;

            }
    }
}

static class Stack {

    static final ArrayList<Integer> stack = new ArrayList<Integer>();

    void push(int x) {
        stack.add(x);
    }

    int pop() {
        int currentSize = stack.size();
        int result;
        if (currentSize == 0) {
            return -1;
        }
        result = stack.get(currentSize-1);

        delete(currentSize-1);

        return result;
    }

    int size() {
        return stack.size();
    }

    int empty() {
        if (size() == 0) {
            return 1;
        }
        return 0;
    }

    int top() {
        int topIndex = size();

        if (topIndex != 0) {
            return stack.get(topIndex-1);
        }
        return -1;
    }

    void delete(int index) {
        stack.remove(index);
    }
    }
}
