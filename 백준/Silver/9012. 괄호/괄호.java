import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        StringBuilder out = new StringBuilder();

        for (int i = 0; i < a; i++){
            String s = br.readLine().trim();
            out.append(isVPS(s) ? "YES" : "NO").append('\n');
        }
        System.out.print(out.toString());
    }
    private static boolean isVPS(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for(int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if(ch == '('){
                stack.push(ch);
            } else if (ch == ')') {
                if (stack.isEmpty()) return false;
                stack.pop();
            } else {

            }
        }
        return stack.isEmpty();
    }
}