public class Crypto {
    public static void main(String[] args) {
        String text = "This is some \"really\" great. (Text)!?";
        int shift = -17;
        int size = 30;
        String encryptedMessage = encryptString(text, shift, size);
        System.out.println(encryptedMessage);
        String originalText = decryptString(encryptedMessage, shift);
        System.out.println(originalText);

    }
    public static String normalizeText(String text) {
        String output = text.replaceAll("[^a-zA-Z]","");
        return output;
    }
    public static String shiftAlphabet(int shift, String alphabet) {
        String shiftedAlphabet = "";
        shift = shift%26;
        if (shift < 0) {
            shift += 26;
        }
        int shiftIndex;
        for (char i = 'a'; i<='z'; i++) {
            shiftIndex = alphabet.indexOf(i) + shift;
            if (shiftIndex>25 && alphabet.indexOf(i) <26) {
                shiftIndex -= 26;
            }
            shiftedAlphabet += alphabet.substring(shiftIndex, shiftIndex + 1);
        }
        for (char i ='A'; i<='Z'; i++) {
            shiftIndex = alphabet.indexOf(i) + shift;
            if (shiftIndex>51 && alphabet.indexOf(i) > 25 && alphabet.indexOf(i) <52) {
                shiftIndex -= 26;
            }
            shiftedAlphabet += alphabet.substring(shiftIndex, shiftIndex + 1);
        }
        return shiftedAlphabet;
    }
    public static String shiftedText(String squished,int shift) {
        String alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String shiftedAlphabet = shiftAlphabet(shift, alphabet);
        String shiftedText = "";
        for (int i = 0; i<squished.length(); i++) {
            int originalID = alphabet.indexOf(squished.substring(i,i+1));
            shiftedText += shiftedAlphabet.charAt(originalID);
        }
        return shiftedText;
    }
    public static String groupify (String text, int size) {
        String groupedText = "";
        int numHold = 0;
        for (int i = 0; i <= (text.length() - size); i += size) {
            groupedText += text.substring(numHold, numHold+size) + " ";
            numHold += size;
            if (((i+size) > (text.length()-size)) && (text.length()%size != 0 )){
                groupedText +=  text.substring(numHold);
                for (int j = size; j > text.length()-(i+size); j--) {
                    groupedText += "8";
                }
            }
        }
        if (size > text.length()) {
            groupedText += text;
            for (int i = 0; i < size - text.length();i++) {
                groupedText += 8;
            }
        }
        return groupedText;
    }
    public static String encryptString (String text, int shift, int group) {
        String squished = normalizeText(text);
        String codeMessage = shiftedText(squished,shift);
        String groupedMessage = groupify(codeMessage, group);
        return groupedMessage;
    }
    public static String decryptString (String text, int shift) {
        String squished = normalizeText(text);
        String codeMessage = shiftedText(squished,shift*(-1));
        return codeMessage;
    }
}
