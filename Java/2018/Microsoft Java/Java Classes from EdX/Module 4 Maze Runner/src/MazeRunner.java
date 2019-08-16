import java.util.Scanner;

public class MazeRunner {
    public static void main(String[] args) {
        Maze myMap = new Maze();
        intro(myMap);
        int initMoves = 200;
        int movesLeft = initMoves;
        while (!myMap.didIWin()) {
            movement(myMap);
            movesLeft -= 1;
            movesMessage(movesLeft, initMoves);
            if (movesLeft == 0) {
                break;
            }
        }
        if (myMap.didIWin()) {
            System.out.println("Congratulations, you made it out alive!");
            System.out.println("and you did it in "+(initMoves-movesLeft)+"moves!");
        } else if (movesLeft == 0) {
            System.out.println("Sorry, but you didn't escape in time- you lose!");
        }
    }
    public static void intro(Maze myMap) {
        System.out.println("\nWelcome to Maze Runner! \nHere is your current position:");
        myMap.printMap();
        System.out.println("---------------------------------------");
    }
    public static void movement(Maze myMap) {
        boolean moveCheck = false;
        Scanner input = new Scanner(System.in);
        while (!moveCheck) {
            System.out.println("Where would you like to move? (R, L, U, D)");
            String playerMove = input.next();
            if ((playerMove.equals("R")) || (playerMove.equals("L")) ||
                    (playerMove.equals("U")) || (playerMove.equals("D"))) {
                boolean pitCheck = navigatePit(playerMove, myMap, input);
                if (pitCheck == false) {
                    moveCheck = true;
                    if (playerMove.equals("R") && myMap.canIMoveRight()) {
                        myMap.moveRight();
                    } else if (playerMove.equals("L") && myMap.canIMoveLeft()) {
                        myMap.moveLeft();
                    } else if (playerMove.equals("U") && myMap.canIMoveUp()) {
                        myMap.moveUp();
                    } else if (playerMove.equals("D") && myMap.canIMoveDown()) {
                        myMap.moveDown();
                    } else {
                        moveCheck = false;
                        System.out.println("You've hit a wall! Please choose again.\n");
                    }
                }
            } else {
                System.out.println("Please choose one of the four allowed directions.");
            }
        } myMap.printMap();
    }
    public static void movesMessage (int movesLeft, int initMoves) {
        if (movesLeft == initMoves*0.5) {
            System.out.println("Warning, you've made "+(initMoves-movesLeft)+" moves. You only have "+movesLeft+
                    " remaining before the maze closes");
        } else if (movesLeft == initMoves*0.25) {
            System.out.println("Alert! You have made "+(initMoves-movesLeft)+" moves, you only have "+movesLeft+
                    " moves left to escape.");
        } else if (movesLeft == initMoves*0.1) {
            System.out.println("DANGER! You have made "+(initMoves-movesLeft)+" moves, you only have "+movesLeft+
                    " moves left to escape!!");
        } else if (movesLeft == 0) {
            System.out.println("Oh no! You took too long to escape, and now the maze exit is closed FOREVER >:[");
        }

    }
    public static boolean navigatePit (String playerMove, Maze myMap, Scanner input) {
        boolean isPitJumped = true;
        if (myMap.isThereAPit(playerMove)) {
            System.out.println("Watch out! There's a pit ahead, jump it?");
            String pitJump = input.next();
            if (pitJump.substring(0,1).equals("y") || pitJump.substring(0,1).equals("Y")) {
                myMap.jumpOverPit(playerMove);
                myMap.printMap();
                return isPitJumped;
            } else {
                return isPitJumped;
            }
        } else {
            isPitJumped = false;
            return isPitJumped;
        }
    }
}
