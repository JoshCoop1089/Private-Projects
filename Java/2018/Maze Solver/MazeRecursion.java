/**
 * @Author: Josh Cooper
 * @Date:   2018-10-12T13:10:28-04:00
 * @Email:  joshcoop1089@gmail.com
 * @Last modified by:   Josh Cooper
 * @Last modified time: 2018-11-19T09:19:05-05:00
 * 
 * New Modifications 4/19/2019 -> Learned DFS Algorithm in CS112
 * 		will use idea of graph connections and visited node information
 * 		and path choice to prove random maze is solvable

 * 
 * Point of this program:
      Ideally, the mazeRunner method will be used to prove
      a maze created by randomMazeMaker is a solvable maze
 */


import java.util.*;
public class MazeRecursion {

  //General Maze Creators/Outputs
  public static char[][] mazeMaker(int size) {
    char[][] maze = new char[size][size];

    //Empty Maze Spots
    for (int i = 1; i < maze.length-1; i++) {
      for (int j = 1; j < maze.length-1; j++) {
        maze[i][j] = '.';
      }
    }

    //Pretty Corners because aethestics
    maze[0][0] = '/';
    maze[0][maze.length-1] = '\\';
    maze[maze.length-1][0] = '\\';
    maze[maze.length-1][maze.length-1] = '/';

    //Outer walls
    for (int i = 1; i < maze.length-1; i++) {
      maze[0][i] = '-';
      maze[maze.length-1][i] = '-';
      maze[i][maze.length-1] = '|';
      maze[i][0] = '|';
    }

    //Adds the wall characters to a collection for easier checking
    wallSet = wallAdd(wallSet);
    return maze;
  }
  public static char[][] mazeExit(char[][] maze) {

    /*Going to need to make specific rules to ensure exit isn't blocked
    by walls from either snake or randomMaze*/
    if ((maze.length+2)%4 == 0) {
      maze[maze.length-1][1] = 'o';
    } else {
      maze[maze.length-1][maze.length-2] = 'o';
    }

    //Forcing an entrance to the maze
    maze[1][0] = '0';
    maze[1][1] = '.';

    return maze;
  }
  public static void mazePrint(char[][] maze) {
    for (int i = 0; i < maze.length; i++) {
      for (int j = 0; j < maze.length; j++) {
        System.out.print(maze[i][j] + " ");
      }System.out.println();
    }
  }

  //Different Maze Types
  public static char[][] snakeMazeMaker(int size) {

    /*Creates an alternating wall pattern to check whether mazeRunner
    can go in every direction */
    char[][] maze = mazeMaker(size);
    for (int i = 1; i < maze.length-2; i++) {
      for (int j = 2; j < maze.length; j += 4) { //Left justified
        maze[j][i] = '-';
      }
      for (int k = 4; k < maze.length; k += 4) { // Right justified
        maze[k][maze.length -(1+i)] = '-';
      }
    }
    maze = mazeExit(maze);
    return maze;
  }
  public static char[][] tCornerMazeMaker() {

    /*Arbitrarily created maze to check all types of movements in one sitting*/
    char[][] maze = mazeMaker(6);
    maze[2][1] = '-';
    maze[2][3] = '-';
    maze[2][4] = '-';
    maze[3][3] = '|';
    maze[4][3] = '|';
    maze = mazeExit(maze);
    return maze;
  }
  public static char[][] randomMazeMaker(int size) {

    //Creates a shotgun style random wall placement maze, because why not
    char[][] maze = mazeMaker(size);
    Random num = new Random();
    int rowNum = 0;
    int columnNum = 0;
    int wallCount = 0;
    double maxWalls = Math.pow((maze.length - 3),2);

    //Placing walls within the confines of the outer walls by using the size-2 modulus
    while (wallCount < maxWalls) {
      rowNum = Math.abs(num.nextInt());
      columnNum = Math.abs(num.nextInt());
      rowNum = rowNum%(size-2) + 1;
      columnNum = columnNum%(size-2) + 1;
      maze[rowNum][columnNum] = '-';
      wallCount++;
    }

    //Will need specific exit rules to make sure there are no random wall covering the exit
    maze = mazeExit(maze);
    return maze;
  }
  
  //Proving the randomly created maze is solvable
  public static boolean isPathAvailable(char[][] maze) {
	  
	  return false;
  }

  //Organizing the wall characters
  public static Set<Character> wallSet = new HashSet<Character>();
  public static Set<Character> wallAdd(Set<Character> walls) {
    walls.add('|');
    walls.add('-');
    walls.add('/');
    walls.add('\\');
    return walls;
  }

  // /*Movement Checks with forced history checking (possibly obsolete
  //           after creation of allowedMovementMap)
  // This version allows the mazeRunner to solve snakeMaze, but not tCornerMaze*/
  // public static boolean canGoUp(char[][] maze, int row, int column) {
  //   if (wallSet.contains(maze[row-1][column]) || maze[row-1][column] == '*') {
  //     return false;
  //   } else {
  //     return true;
  //   }
  //
  // }
  // public static boolean canGoDown(char[][] maze, int row, int column) {
  //   if (wallSet.contains(maze[row+1][column]) || maze[row+1][column] == '*') {
  //     return false;
  //   } else {
  //     return true;
  //   }
  // }
  // public static boolean canGoLeft(char[][] maze, int row, int column) {
  //   if (wallSet.contains(maze[row][column-1]) || maze[row][column-1] == '*') {
  //     return false;
  //   } else {
  //     return true;
  //   }
  // }
  // public static boolean canGoRight(char[][] maze, int row, int column) {
  //   if (wallSet.contains(maze[row][column+1]) || maze[row][column+1] == '*') {
  //     return false;
  //   } else {
  //     return true;
  //   }
  // }

  /*Movement Checks (Generic Version with error catching)
  This version is a good base to tinker with*/
  public static boolean canGoUp(char[][] maze, int row, int column) {
    try {
      if (wallSet.contains(maze[row-1][column])) {
        return false;
      } else {
        return true;
      }
    } catch (Exception e) {
        return false;
    }
  }
  public static boolean canGoDown(char[][] maze, int row, int column) {
    try {
      if (wallSet.contains(maze[row+1][column])) {
        return false;
      } else {
          return true;
      }
    } catch (Exception e) {
          return false;
    }
  }
  public static boolean canGoLeft(char[][] maze, int row, int column) {
    try {
      if (wallSet.contains(maze[row][column-1])) {
        return false;
      } else {
        return true;
      }
    } catch (Exception e) {
      return false;
    }
  }
  public static boolean canGoRight(char[][] maze, int row, int column) {
    try {
      if (wallSet.contains(maze[row][column+1])) {
        return false;
      } else {
        return true;
      }
    } catch (Exception e) {
          return false;
    }
  }

  //First attempt at deleting taken paths
  public static HashMap<String, char[]> allowedMovementMap = new HashMap<String, char[]>();
  public static void allowedMovement(char[][] maze) {
    for (int row = 1; row < maze.length - 1; row++) {
      for (int column = 1; column < maze.length - 1; column++) {
        String location = Integer.toString(row) + Integer.toString(column);
        char[] allowedDirection = {'0','0','0','0'};
        if (canGoRight(maze, row, column)) {
          allowedDirection[0] = 'r';
        }
        if (canGoDown(maze, row, column)) {
          allowedDirection[1] = 'd';
        }
        if (canGoLeft(maze, row, column)) {
          allowedDirection[2] = 'l';
        }
        if (canGoUp(maze, row, column)) {
          allowedDirection[3] = 'u';
        }
        allowedMovementMap.put(location, allowedDirection);
      }
    }
    char[] allowedDirection = {'r','0','0','0'};
    allowedMovementMap.put("10", allowedDirection);
  }
  public static void replacePossibleMoves(HashMap<String, char[]>
                                allowedMovementMap, int i, String location) {
    char[] possibleMoves = allowedMovementMap.get(location);
    possibleMoves[i] = '0';
    allowedMovementMap.put(location, possibleMoves);
  }


  //Main Runner Function
  public static void mazeRunner(char[][] maze, int row, int column, int recursionCounter) {
    //Personal OHSHIT loop so it doesn't wipe out the console with errors when it screws up
    if (recursionCounter > 25) {
      System.out.println("Max recursions allowed");
      return;
    }
    recursionCounter++;

    //Look at the pretty maze!
    System.out.println("\nStep " + (recursionCounter - 1) + ":");
    mazePrint(maze);

    //Exit Check will need to be rewritten when I figure out how to properly code randomMaze
    if (((maze.length+2)%4 == 0 && row == maze.length-1 && column == 1)
          || (row == maze.length-1 && column == maze.length-2)) {
      System.out.println("You made it out!");
      return;
    }

    String location = Integer.toString(row) + Integer.toString(column);

    //Used to show path through maze
    maze[row][column]='*';

    /*Shows me the internal move possiblities so I can check them, delete in final*/
    allowedMovementMap.forEach((k,v) -> System.out.println(
            k + "=" + Arrays.toString(allowedMovementMap.get(k))));

    //Actual Movement Portion
    if (allowedMovementMap.get(location)[0] == 'r') { //Go Right
      maze[row][column+1] = '#';
      replacePossibleMoves(allowedMovementMap, 0, location);
      mazeRunner(maze, row, column+1, recursionCounter);
    } else if (allowedMovementMap.get(location)[1] == 'd') { //Go Down
      maze[row+1][column] = '#';
      replacePossibleMoves(allowedMovementMap, 1, location);
      mazeRunner(maze, row+1, column, recursionCounter);
    } else if (allowedMovementMap.get(location)[2] == 'l') { //Go Left
      maze[row][column-1] = '#';
      replacePossibleMoves(allowedMovementMap, 2, location);
      mazeRunner(maze, row, column-1, recursionCounter);
    } else if (allowedMovementMap.get(location)[3] == 'u'){ //Go Up
      maze[row-1][column] = '#';
      replacePossibleMoves(allowedMovementMap, 3, location);
      mazeRunner(maze, row-1, column, recursionCounter);
    } else {
      System.out.println("We've hit a bug!");
      return;
    }

    /*Old version of the move commands, blended into the allowedMovement
     function, kept just in case*/

    // if (canGoRight(maze, row, column)) {
    //   maze[row][column+1] = '#';
    //   mazeRunner(maze, row, column+1, recursionCounter);
    // } else if (canGoDown(maze, row, column)) {
    //   maze[row+1][column] = '#';
    //   mazeRunner(maze, row+1, column, recursionCounter);
    // } else if (canGoLeft(maze, row, column)) {
    //   maze[row][column-1] = '#';
    //   mazeRunner(maze, row, column-1, recursionCounter);
    // } else if (canGoUp(maze, row, column)) {
    //   maze[row-1][column] = '#';
    //   mazeRunner(maze, row-1, column, recursionCounter);
    // } else {
    //   System.out.println("we hit a bug!");
    //   return;
    // }
  }

  public static void main(String[] args) {

    System.out.println("\nWelcome to the Recursive Runner!\n");
    System.out.println("\nA '|' or a '-' represent a wall, an 'o' shows an exit"
                        +"\n\tand a '.' shows an empty unexplored square."
                        +"\n\tA previously visited square is marked as a '*'"
                        +"\n\tand your current location is shown with a '#'");

    // System.out.println("\nWhat size square maze do you want?"
    //                     +"\n\t**Reminder, a maze size over 7 will trip the"
    //                     +"\n\tcurrent recursion limit, and less than 3 will"
    //                     +"\n\tmake the maze too small.**"
    //                     +"\n\nEnter a number greater than or equal to 3: ");

    // Scanner input = new Scanner(System.in);
    // int size = input.nextInt();
    // while (size < 3) {
    //   System.out.println("If you use a number less than 3, the maze doesn't print"
    //                     +" properly, why are you being obstinate?");
    //   size = input.nextInt();
    // }

    int recursionCounter = 0;
    int startRow = 1;
    int startColumn = 0;

    // //Snake tests if runner can go left consistently while right is the first listed movement
    // char[][] maze = snakeMazeMaker(size);
    // allowedMovement(maze);
    // mazeRunner(maze, startRow, startColumn, recursionCounter);

    /*TCorner tests if runner can move R -> R -> R -> L -> D
    showing that it can backtrack and choose a different path */
    char[][] triMaze = tCornerMazeMaker();
    allowedMovement(triMaze);
    mazeRunner(triMaze, startRow, startColumn, recursionCounter);

    // //End goal is to prove a randomly created maze is solvable
    // char[][] ranMaze = randomMazeMaker(size);
    // allowedMovement(ranMaze);
    // mazeRunner(ranMaze, startRow, startColumn, recursionCounter);
  }
}
