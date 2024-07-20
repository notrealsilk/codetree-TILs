import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next(); // 문자열로 입력 받기
        
        // 문자열을 '-'로 구분하여 배열로 나누기
        String[] parts = input.split("-");
        
        // 배열에서 각 부분을 정수로 변환
        String a = parts[0]; // 앞의 숫자
        String b = parts[1]; // 두 번째 숫자
        String c = parts[2]; // 세 번째 숫자
        
        // Swap b and c
        String temp = b;
        b = c;
        c = temp;
        
        // Print the result in the format a-b-c
        System.out.println(a + "-" + b + "-" + c);
    }
}