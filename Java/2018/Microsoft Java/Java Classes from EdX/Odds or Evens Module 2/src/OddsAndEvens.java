import java.util.*;
public class OddsAndEvens {
    public static void main(String[] args) {
        boolean gameOver = false;
        while (gameOver == false) {
            Scanner input = new Scanner(System.in);
            System.out.println("\nLet's play a game called \"Odds and Evens\"");
            System.out.print("What is your name? ");
            String name = input.nextLine();
            boolean chosen = false;
            String choice = "";
            String compChoice = "";

            //Game Initialization Loop
            while (chosen == false) {
                System.out.print("Hi " + name + ", which do you choose? (O)dds or (E)vens? ");
                choice = input.next();
                if (choice.equals("e") || choice.equals("E")) {
                    choice = "evens";
                    compChoice = "odds";
                    chosen = true;
                } else if (choice.equals("o") || choice.equals("O")) {
                    choice = "odds";
                    compChoice = "evens";
                    chosen = true;
                } else {
                    System.out.println("what are you doing, you know the rules here?!?!");
                }
            }
            System.out.println(name+" has picked "+choice+"! The computer will be "+compChoice+".");
            System.out.println("-------------------------------------------------\n");

            //Main Game Input
            System.out.print("How many \"fingers\" do you put out? ");
            int fingers = input.nextInt();
            Random rand = new Random();
            int computer = rand.nextInt(6);
            System.out.println("The computer plays "+computer+" \"fingers\".");
            System.out.println("-------------------------------------------------\n");

            int sum = fingers+computer;
            String oddEven = "";
            if (sum%2 == 0) {
                oddEven = "even!";
            }
            else {
                oddEven = "odd!";
            }
            String winner = "";
            if ((oddEven.equals("even!") && choice.equals("evens"))
                    || (oddEven.equals("odd!") && choice.equals("odds"))) {
                winner = name;
            } else {
                winner = "the computer";
            }
            System.out.println(fingers+" + "+computer+" = "+sum);
            System.out.println(sum+" is ... "+oddEven);
            System.out.println("That means "+winner+" wins! :)");
            System.out.println("-------------------------------------------------\n");

            //Replay and Game Over checks
            boolean replayCheck = false;
            while (replayCheck == false) {
                System.out.print("Would you like to play again? (Y)es or (N)o? ");
                String replay = input.next();
                if (replay.equals("n") || replay.equals("N")) {
                    replayCheck = true;
                    gameOver = true;
                    System.out.println("Thanks for playing!");
                } else if (replay.equals("y") || replay.equals("Y")) {
                    replayCheck = true;
                    System.out.println("Okay, starting the game again!");
                } else {
                    System.out.println("the fuck, you know the rules...");
                }
            }
        }
    }
}
