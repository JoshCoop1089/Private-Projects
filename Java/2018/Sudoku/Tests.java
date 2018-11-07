/**
 * @Author: Josh Cooper
 * @Date:   2018-11-01T12:01:08-04:00
 * @Email:  joshcoop1089@gmail.com
 * @Last modified by:   Josh Cooper
 * @Last modified time: 2018-11-07T13:43:29-05:00
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
    small.currentBoardState();
    small.boardPrint();
    int row = 1;
    int column = 3;
    int number = 2;
    int box = Board.boxChoose(row, column, small.getNum());
    System.out.println("Row " + row + " was: \t" +
                  Arrays.toString(small.getBoardState("Row " + row)));
    System.out.println("Column " + column + " was: \t" +
                  Arrays.toString(small.getBoardState("Column " + column)));
    System.out.println("Box " + box + " was: \t" +
                  Arrays.toString(small.getBoardState("Box " + box)));
    small.placeNumber(row,column,number);
    System.out.println("Row " + row + " is now: \t" +
                  Arrays.toString(small.getBoardState("Row " + row)));
    System.out.println("Column " + column + " is now:\t" +
                  Arrays.toString(small.getBoardState("Column " + column)));
    System.out.println("Box " + box + " is now: \t" +
                  Arrays.toString(small.getBoardState("Box " + box)));
    small.boardPrint();
  }
}
