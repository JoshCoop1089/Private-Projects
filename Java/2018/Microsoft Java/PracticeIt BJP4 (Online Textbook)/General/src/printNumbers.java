public class printNumbers {
    public static void main(String[] args) {
        printNumber(5);
        printNumber(1);
        printNumber(10);
    }
    public static void printNumber(int number) {
        for (int i = 0; i < number; i++) {
            System.out.print("[" + (i+1) + "] ");
        }
        System.out.println();
    }
}
