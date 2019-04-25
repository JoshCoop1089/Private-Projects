package mazeObjects;

import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class MazeBoard {
	int size;
	char boardType;
	Node[][] mazeBase = null;
	Scanner input = new Scanner(System.in);
	
	/*
	 * DFS Ideas
	 * 
	 * Since every node contains its link possibilities, scan the rows and columns from 1 to length - 1, 
	 * and then use DFS on the left, down, right up nodes in order.  When you start the function, mark a node as visited
	 */
	public void setAdjancency() {
		for (int i = 1; i < size - 1 ; i++) {
			for (int j = 1; j < size - 1 ; j++) {
				Node currentTile = mazeBase[i][j];
				System.out.println(currentTile.tileValue);
				
				//Check availability only for tiles which are empty, automatically leaving walls as unreachable by dfs
				if (currentTile.tileValue == '.') {
//					System.out.println(currentTile + " is empty, k");
					if (mazeBase[i][j-1].tileValue == '.' || mazeBase[i][j-1].tileValue == 'o') currentTile.leftAvailable = true;	
					if (mazeBase[i][j+1].tileValue == '.' || mazeBase[i][j+1].tileValue == 'o') currentTile.rightAvailable = true;
					if (mazeBase[i+1][j].tileValue == '.' || mazeBase[i+1][j].tileValue == 'o') currentTile.upAvailable = true;
					if (mazeBase[i-1][j].tileValue == '.' || mazeBase[i-1][j].tileValue == 'o') currentTile.downAvailable = true;
				}
			}
		}
	}
	
	public void dfs(int row, int column) {
		Node currentNode = mazeBase[row][column];
		currentNode.tileValue = 'x';
		System.out.println("\nStarting dfs from  Row " + row + " Column " + column);
		System.out.println(this);
		
		//Checking if a location has been seen before, otherwise marking as seen
		if (currentNode.visited) {
			System.out.println("\tAlready visited here");
			return;
		}
		else currentNode.visited = true;
		
		//Checking if we are at the end
		if (currentNode.tileValue == 'o') {
			System.out.println("goal reached!");
			return;
		}
		
		//Advancing deeper into the maze
		if (currentNode.leftAvailable && mazeBase[row][column-1].visited == false) {
			System.out.println("Now visiting Row " + row + " Column " + (column - 1));
			this.dfs(row,column-1);
		}
		if (currentNode.rightAvailable && mazeBase[row][column+1].visited == false) {
			System.out.println("Now visiting Row " + row + " Column " + (column + 1));
			this.dfs(row,column+1);
		}
		if (currentNode.upAvailable && mazeBase[row-1][column].visited == false) {
			System.out.println("Now visiting Row " + (row + 1) + " Column " + column);
			this.dfs(row+1,column);
		}
		if (currentNode.downAvailable && mazeBase[row+1][column].visited == false) {
			System.out.println("Now visiting Row " + (row - 1) + " Column " + column);
			this.dfs(row-1,column);
		}
		
		System.out.println("no where to go from Row " + row + " Column " + column);
		return;
	}
	
	MazeBoard(int size, char boardType) {
		this.size = size;
		switch(boardType) {
			case 'r':
				System.out.println("\nMaking a Random maze of size " + size);
				mazeBase = randomMazeMaker(size);
				break;
			case 's':
				System.out.println("\nMaking a Snake maze of size " + size);
				mazeBase = snakeMazeMaker(size);
				break;
			case 't':
				mazeBase = tCornerMazeMaker();
				break;
		}
		this.setAdjancency();
	}
	
	  //General Maze Creators/Outputs
	  public static Node[][] mazeMaker(int size) {
		
	    Node[][] maze = new Node[size][size];

	    //Empty Maze Spots
	    for (int i = 1; i < maze.length-1; i++) {
	      for (int j = 1; j < maze.length-1; j++) {
	    	  maze[i][j] = new Node('.');
	      }
	    }

	    //Pretty Corners because aethestics
	    maze[0][0] = new Node('/');
	    maze[0][maze.length-1] = new Node('\\');
	    maze[maze.length-1][0] = new Node('\\');
	    maze[maze.length-1][maze.length-1] = new Node('/');

	    //Outer walls
	    for (int i = 1; i < maze.length-1; i++) {
	      maze[0][i] = new Node('-');
	      maze[maze.length-1][i] = new Node('-');
	      maze[i][maze.length-1] = new Node('|');
	      maze[i][0] = new Node('|');
	    }

	    //Adds the wall characters to a collection for easier checking
	    wallSet = wallAdd(wallSet);
	    return maze;
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
	  
	  public static Node[][] mazeExit(Node[][] maze) {

	    /*Going to need to make specific rules to ensure exit isn't blocked
	    by walls from either snake or randomMaze*/
	    if ((maze.length+2)%4 == 0) {
	      maze[maze.length-1][1] = new Node('o');
	    } else {
	      maze[maze.length-1][maze.length-2] = new Node('o');
	    }

	    //Forcing an entrance to the maze
	    maze[1][0] = new Node('0');
	    maze[1][1] = new Node('.');

	    return maze;
	  }


	  //Different Maze Types
	  public static Node[][] snakeMazeMaker(int size) {

	    /*Creates an alternating wall pattern to check whether mazeRunner
	    can go in every direction */
	    Node[][] maze = mazeMaker(size);
	    for (int i = 1; i < maze.length-2; i++) {
	      for (int j = 2; j < maze.length; j += 4) { //Left justified
	        maze[j][i] = new Node('-');
	      }
	      for (int k = 4; k < maze.length; k += 4) { // Right justified
	        maze[k][maze.length -(1+i)] = new Node('-');
	      }
	    }
	    maze = mazeExit(maze);
	    return maze;
	  }
	  
	  public static Node[][] tCornerMazeMaker() {

	    /*Arbitrarily created maze to check all types of movements in one sitting*/
	    Node[][] maze = mazeMaker(6);
	    maze[2][1] = new Node('-');
	    maze[2][3] = new Node('-');
	    maze[2][4] = new Node('-');
	    maze[3][3] = new Node('|');
	    maze[4][3] = new Node('|');
	    maze = mazeExit(maze);
	    return maze;
	  }
	  public static Node[][] randomMazeMaker(int size) {

	    //Creates a shotgun style random wall placement maze, because why not
	    Node[][] maze = mazeMaker(size);
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
	      maze[rowNum][columnNum] = new Node('-');
	      wallCount++;
	    }

	    //Will need specific exit rules to make sure there are no random wall covering the exit
	    maze = mazeExit(maze);
	    return maze;
	  }
	  
		@Override
		public String toString() {
		    for (int i = 0; i < mazeBase.length; i++) {
		      for (int j = 0; j < mazeBase.length; j++) {
		    	  System.out.print(mazeBase[i][j] + " ");
		      }System.out.println();
		    }
			return "";
		}

}
