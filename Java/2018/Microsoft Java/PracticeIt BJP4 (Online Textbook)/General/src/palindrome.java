import java.util.Scanner;

public class palindrome {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        for (int i = 0; i < 2; i++) {
            printPalindrome(input);
        }
    }
    public static void printPalindrome (Scanner input) {
        System.out.print("Type one or more words: ");
        String word = input.nextLine();
        String wordCollapse = word.replaceAll("\\s","");
        String lowerWord = wordCollapse.toLowerCase();
        boolean palCheck = true;
        for (int i = 0; i < lowerWord.length()/2; i++) {
            if (lowerWord.charAt(i) == lowerWord.charAt(lowerWord.length()-(i+1))) {
                palCheck = true;
            } else {
                palCheck = false;
                break;
            }
        }
        if (palCheck == true) {
            System.out.println(word+" is a palindrome!");
        }
        if (palCheck == false) {
            System.out.println(word+" is not a palindrome.");
        }
    }
}
