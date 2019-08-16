public class verticalPrint {
    public static void main(String[] args) {
        vertical("hey now");
    }
    public static void vertical (String phrase) {
        for (int i = 0; i < phrase.length(); i++) {
            String letter = phrase.substring(i, i+1);
            System.out.println(letter);
        }
    }
}
