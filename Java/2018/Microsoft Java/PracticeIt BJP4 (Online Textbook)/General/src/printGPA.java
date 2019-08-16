import java.util.Scanner;

public class printGPA {
    public static void main(String[] args) {
        printGPA();
    }
    public static String printGPA() {
        Scanner input= new Scanner(System.in);
        System.out.print("Enter a student record: ");
        String record = input.nextLine();
        String[] info = record.split(" ");
        String name = info[0];
        System.out.println(name);
        int numberOfGrades = Integer.parseInt(info[1]);
        System.out.println(numberOfGrades);
        double gradeSum = 0;
        for (int i = 2; i < info.length; i++) {
            gradeSum += Integer.parseInt(info[i]);
        }
        double average = gradeSum/numberOfGrades;
        System.out.println(average);
        String output = name+"'s grade is "+average;
        System.out.println(output);
        return output;
    }
}
