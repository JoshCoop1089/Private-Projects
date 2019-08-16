public class firstSecondTwo {
    public static void main(String[] args) {
        firstSecondAlpha();
        firstSecondBeta ();
    }
    public static void firstSecondAlpha () {
        int first = 8;
        int second = 19;
        first = first + second;
        second = first - second;
        first = first - second;
        System.out.println("First: " + first);
        System.out.println("Second: " + second);
    }
    public static void firstSecondBeta () {
        int first=8, second=19;
        first += second;
        second = first - second;
        first -= second;
        System.out.println("First: " + first);
        System.out.println("Second: " + second);
    }
}
