import java.util.Scanner;
import java.io.*;
public class LoopPractice {
    public static void main(String []argh){

        int t= 1;
        for(int i=0;i<t;i++) {
            int a = 37;
            int b = 17;
            int n = 14;
            int total = a;
            for (int j = 0; j < n; j++) {
                total += b * Math.pow(2, j);
                System.out.print(total);
                if (i < (n - 1)) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}

