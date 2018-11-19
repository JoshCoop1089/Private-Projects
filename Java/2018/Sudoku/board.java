/**
 * @Author: Josh Cooper
 * @Date:   2018-10-24T08:57:47-04:00
 * @Filename: board.java
 * @Last modified by:   Josh Cooper
 * @Last modified time: 2018-11-19T14:09:39-05:00
 */


import java.util.*;
public class Board {

  //Attributes
  private int num;  //will be required for calculating certain properties for box choice
  private int gameCount; //Used to access specific game boards for UNdo function
  private char difficulty = '';  // for choosing E/M/H versions of 9x9 boards

  //Used for while loops for proper row/column checks
  private boolean rowChosen;
  private boolean columnChosen;
  private boolean numberChosen;

  //Setting up the board arrays for restarting game and managing current board
  private int[][] startBoard;  // should be filled in by FileIO from the premade text files eventually
  private int[][] currentBoard;  // will hold the currentBoard version of the board
  private HashMap<String, int[]> boardState = new HashMap<String, int[]>();
  private HashMap<Integer, int[][]> gameHistory = new HashMap<Integer, int[][]>();


  //Constructor
  public Board(int size, char difficulty) { //Used for 9x9 with difficulty chosen
    this.num = (int) Math.pow(size, 0.5);
    this.startBoard = new int[size][size];
    this.currentBoard = new int[size][size];
    if (difficulty != '') {
      this.difficulty = difficulty;
    }
    this.rowChosen = false;
    this.columnChosen = false;
    this.numberChosen = false;
  }

  //Getters
  public int[] getBoardState(String key) {
    return this.boardState.get(key);
  }
  public int[][] getGameHistory(int num) {
    return this.gameHistory.get(num);
  }
  public int getNum() {
    return this.num;
  }
  public boolean getrowChosen() {
    return this.rowChosen;
  }
  public boolean getColumnChosen() {
    return this.columnChosen;
  }
  public boolean getNumberChosen() {
    return this.numberChosen;
  }

  //Setters

    //This should modify specific keys to update the state when you plug in new numbers
  public void setBoardState(String key, int[] nums) {
    this.boardState.put(key,nums);
  }
  public void setRowChosen(boolean rowChosen) {
    this.rowChosen = rowChosen;
  }
  public void setColumnChosen(boolean columnChosen) {
    this.columnChosen = columnChosen;
  }
  public void setNumberChosen(boolean numberChosen) {
    this.numberChosen = numberChosen;
  }

    //This should take the entire 2dInt array and store it to refer to later via undo function
  public void setGameHistory(int gameCount, int[][] current) {
    this.gameHistory.put(gameCount,current);
  }


  //Methods To Finish
  // public static int chooseSize() {
  //   int size = 0;
  //   try {
  //     System.out.print("Please pick which type of board you want to play."+
  //                       "\n Input 4 for a 4x4 game, or 9 for a 9x9 game."+
  //                       "\n Input 99 to quit. ===> ");
  //   catch (Exception e) {
  //
  //   }
  //   return size;
  // }
  // public static char chooseDifficulty() {
  //   char difficulty = '';
  //   return difficulty;
  // }
  public static void chooseRandomBoard () {}
  public int[][] boardStart() {
    //load board from file, populate this.startBoard with proper digits,
    // populate this.boardState with first set of row,column,box values
    return this.startBoard;
  }
  public static void gameState () {}
  public void chooseNumber(int number) {

  }
  public void chooseRow(int row) {}
  public void chooseColumn(int column) {}
  public void undoMove() {
    System.out.println("The board will now be:\n");
    this.current = this.gameHistory.get(this.gameCount)
    this.boardPrint();
  }


  //Complete Methods
  public void boardPrint() {
    int count = 0;
    int columnHold = 1;
    int columnCount = 0;
    int rowShow = 1;
    String rowOut = "";
    int dashCount = this.num*(3*this.num+3)+1;

    //Create Column Numbers for Header
    Map<Integer, String> columnMap = new HashMap<>();
    while (columnCount < this.num) {
      String columns = "";
      for (int i = columnHold; i < columnHold + num; i++) {
        columns += i + "  ";
      }
      columnMap.put(columnCount,columns);
      columnHold += num;
      columnCount++;
    }
    String columnList = "";
    for (int key: columnMap.keySet()) {
            columnList +=  columnMap.get(key) + "   ";
    }

    //Board Header
    String space = "";
    for(int i = 0; i < dashCount/2; i++) {
      space += " ";
    }
    String dashes = "";
    for (int i = 0; i < dashCount; i++) {
      dashes += "-";
    }
    System.out.println(space + " Column #");
    System.out.println("||Row  " + columnList);
    System.out.println("\\/# " + dashes);

    //Internal Board Parts
    Map<Integer, String> boardChunk = new HashMap<>();
    int numHold = 0;
    for (int i = 0; i < this.currentBoard.length; i++) {
      numHold = 0;
      for (int j = 0; j < num; j++) {
        boardChunk.put(count,Arrays.toString(Arrays.copyOfRange(this.currentBoard[i],numHold, num + numHold)));
        count++;
        numHold += num;
      }
    }
    numHold = 0;
    while (rowShow <= this.currentBoard.length) {
      for (int i = numHold; i < num + numHold; i++) {
        rowOut += " | " + boardChunk.get(i);
      }
      System.out.println("  " + Integer.toString(rowShow) + rowOut + " |");
      numHold += num;
      rowShow++;
      rowOut = "";
      if (rowShow%num == 1) {
        System.out.println("    " + dashes);
      }
    }
  }
  public void currentBoardState() {
    this.currentBoard[1][1] = 2;
    this.currentBoard[0][2] = 4;
    this.currentBoard[3][3] = 6;
    this.currentBoard[2][0] = 8;
    this.currentBoard[2][1] = 2;
    this.currentBoard[0][3] = 4;
    this.currentBoard[2][3] = 6;
    this.currentBoard[1][3] = 8;
    //Internal helper for box aggregation
    HashMap<String, List<Integer>> boxes= new HashMap<>();
    List<Integer> boxHelper = new ArrayList<>();
    //Iterate over tihs.current to create inital values for row,column and box
    for (int i = 0; i < this.currentBoard.length; i++) {
      boardState.put("Row " + Integer.toString(i+1), this.currentBoard[i]); //Row Creator
      int[] helperColumn = new int[this.currentBoard.length];
      for (int j = 0; j < this.currentBoard.length; j++) {
        helperColumn[j] = this.currentBoard[j][i]; //Column Aggregator
        String boxKey = "Box " + Integer.toString(boxChoose(i+1, j+1, num));

        //Prepping boardState for full box transfer
        boardState.put(boxKey, new int[this.currentBoard.length]);

        //Box aggregation
        if (boxes.get(boxKey) == null) {
          boxes.put(boxKey, new ArrayList<>());
        }
        boxHelper = boxes.get(boxKey);
        boxHelper.add(this.currentBoard[i][j]);
        boxes.put(boxKey,boxHelper); // Box Creator
      }
      boardState.put("Column " + Integer.toString(i+1), helperColumn); // Column Creator
    }

    //Transfer final box list from helper to main boardState
    for (int i = 0; i < this.currentBoard.length; i++) {
      for (String key : boxes.keySet()) {
        boardState.get(key)[i] = boxes.get(key).get(i);
      }
    }
    boardState.forEach((k,v) -> System.out.println(
                    k + " = " + Arrays.toString(boardState.get(k))));
  }
  public static int boxChoose(int row, int column, int num) {
     int rowChunk = ((row-1)/num)+1;
     int columnChunk = ((column - 1)/num)+1;
     int boxNumber = num*(rowChunk-1)+columnChunk;
     return boxNumber;
  }
  public boolean rowUnique (int row, int number) {
      boolean rowUnique = true;
      for (int i : this.boardState.get("Row " + row)) {
          if (i == number) {
              rowUnique = false;
          }
      } return rowUnique;
  }
  public boolean boxUnique (int box, int number) {
      boolean boxUnique = true;
      for (int i : this.boardState.get("Box "+ box)) {
          if (i == number) {
              return false;
          }
      } return boxUnique;
  }
  public boolean columnUnique (int column, int number) {
      boolean columnUnique = true;
      for (int i : this.boardState.get("Column " + column)) {
          if (i == number) {
              return false;
          }
      } return columnUnique;
  }
  public int[] replaceNumber(int[] arrayHelper, int numHold, int number) {
    for (int i = 0; i < arrayHelper.length; i++) {
      if (arrayHelper[i] == numHold) {
        arrayHelper[i] = number;
        break;
      }
    }
    return arrayHelper;
  }
    //this version of placeNumber assumes valid placement
  public void placeNumber(int row, int column, int number) {
    //Holding the number to check inside the replaceNumber function
    int numHold = this.currentBoard[row-1][column-1];

    //Put the number in the Row Key
    int[] arrayHelper = this.getBoardState("Row " + row);
    arrayHelper = this.replaceNumber(arrayHelper, numHold, number);
    this.setBoardState("Row " + row, arrayHelper);

    //Puts the number in the Column Key
    arrayHelper = this.getBoardState("Column " + column);
    arrayHelper = this.replaceNumber(arrayHelper, numHold, number);
    this.setBoardState("Column " + column, arrayHelper);

    //Puts the number in the Box Key
    arrayHelper = this.getBoardState("Box " + boxChoose(row, column, this.num));
    arrayHelper = this.replaceNumber(arrayHelper, numHold, number);
    this.setBoardState("Box " + boxChoose(row,column,this.num), arrayHelper);
    this.currentBoard[row-1][column-1] = number;

  }


}
