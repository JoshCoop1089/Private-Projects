import java.util.Arrays;
import java.util.Scanner;

public class Sudoku {
    /*
    Stage 1 (Base Game)
    -- Complete --
    Unique Identifiers

    -- To Do --
    Print Board
    Undo
    Number Placement
    Occupied Spot
    Win State

Stage 2 (Practice Data Import)
    -- Complete --


    -- To Do --
    Import premade boards from multiple files
        (chooseBoardSize function)
    Choice of random board of requested size/difficulty
            (4x4 or 9x9 easy,medium,hard)
        (chooseRandom function)

Stage 3 (Hardcoding is bad mkay)
    -- Complete --
    Rework box identification after row column choice for unique checks
        (boxChoose function)

    -- To Do --
    Scalability, reformat code to work for board size n^2
        (Include 4x4,9x9 test cases)
    Rework box identification code to create box list on fly
        (currentState function)
    Rework box identification for boardPrint function
        (boardPrint function)


Stage 3a (Update base game code)
    Rewrite Stage 1 game with Stage 2/3 additions
    Replay feature with new board import from file

Stage 3b (Optimize base code and clean up writing)
    Switch boardDict function to non quadratic version, attempt to use linear
        version of coding by figuring out a way to replace single values instead
        of recreating full dict every round
    Erase duplicates in error messages
    Change win function to identify lack of zeros on board instead of using boardDictSort?
    Go through another round of glassbox error checks to make sure that all paths
        are clean, no new bugs from old copies
    Create board class and rewrite function to use methods instead of overt
        loops on regular objects

Stage 4 (Multiple Language Practice, syntax doesn't change logic flow)
    (ETA July)
    Rewrite in Java
        (Such a small step... ffs)
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[][] startBoard = {  {1,2,3,4},
                                {2,3,4,1},
                                {3,4,1,2},
                                {4,1,2,3}};
        int[] columns = new int[4];
        for (int i = 0; i <4; i++) {
            columns[i] = startBoard[0][i];
        }

        System.out.println(Arrays.toString(columns(0,2)));


//        Step 3b Class creation for board actions, separate from main game
//              involving number/row/column picks

//        board startBoard = new board();
//        //Choose the beginning board with error checking for early quit
//        startBoard.boardStart();
//
//        //Built for replay checks after board started
//        startBoard.chooseSize();
//        startBoard.chooseRandom();
//
//        //Shows current state of board
//        startBoard.boardPrint();
//
//        //creates array for use in unique checks
//        startBoard.currentState();
//
//        //creates map for history of gameboards
//        startBoard.gameState();






    }
//    public static int rowChoose (Scanner input, board current) {}
//    public static int columnChoose (Scanner input, board current) {}
//    public static int numberChoose (Scanner input board current) {}
//    public static int boxChoose(int row, int column, int num) {
//        int rowChunk = ((row-1)/num)+1;
//        int columnChunk = ((column - 1)/num)+1;
//        int boxNumber = num*(rowChunk-1)+columnChunk;
//        return boxNumber;
//    }
//    public static boolean rowUnique (int[] row, int number) {
//        boolean rowUnique = true;
//        for (int i : row) {
//            if (i == number) {
//                rowUnique = false;
//            }
//        } return rowUnique;
//    }
//    public static boolean boxUnique (int[] box, int number) {
//        boolean boxUnique = true;
//        for (int i : box) {
//            if (i == number) {
//                return false;
//            }
//        } return boxUnique;
//    }
//    public static boolean columnUnique (int[] column, int number) {
//        boolean columnUnique = true;
//        for (int i : column) {
//            if (i == number) {
//                return false;
//            }
//        } return columnUnique;
//    }
}
