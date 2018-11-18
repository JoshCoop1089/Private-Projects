/**
 * @Author: Josh Cooper
 * @Date:   2018-11-01T12:01:08-04:00
 * @Email:  joshcoop1089@gmail.com
 * @Last modified by:   Josh Cooper
 * @Last modified time: 2018-11-18T11:21:44-05:00
 */
import java.util.*;
public class Tests {
  public static void main(String[] args) {
    // int size = Board.chooseSize();
    // if (size == 9) {}
    // char difficulty = Board.chooseDifficulty();
    // Board test = new Board(9,'e');
    // test.currentState();
    // test.boardPrint();
    Board small = new Board(4,'e');
    small.boardPrint();
    small.currentBoardState();
    small.boardPrint();
    int row = 1;
    int column = 3;
    int number = 2;
    int box = Board.boxChoose(row, column, small.getNum());

    System.out.println("\nTesting Number placement/replacing");
    System.out.println("\nRow " + row + " was: \t" +
                  Arrays.toString(small.getBoardState("Row " + row)));
    System.out.println("Column " + column + " was: \t" +
                  Arrays.toString(small.getBoardState("Column " + column)));
    System.out.println("Box " + box + " was: \t" +
                  Arrays.toString(small.getBoardState("Box " + box)));
    System.out.println("\nPutting " + number + " at Row " + row + " Column " + column);

    small.placeNumber(row,column,number);

    System.out.println("\nRow " + row + " is now: \t" +
                  Arrays.toString(small.getBoardState("Row " + row)));
    System.out.println("Column " + column + " is now:" +
                  Arrays.toString(small.getBoardState("Column " + column)));
    System.out.println("Box " + box + " is now: \t" +
                  Arrays.toString(small.getBoardState("Box " + box))+ "\n");
    small.boardPrint();
  }
}
