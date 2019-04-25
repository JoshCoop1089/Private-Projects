package mazeObjects;

import java.util.Scanner;

public class MazeTester {
	public static void main(String[] args) {
		MazeBoard maze = null;
		char mazeType = ' ';
		int mazeSize = 0;
		Scanner input = new Scanner(System.in);

		while (mazeType == ' ') {
			try {
				System.out.print("What type of maze do you want to try? "
						+ "\n    Enter 'r' for a randomly created maze "
						+ "\n    Enter 't' for a triangle cornered maze "
						+ "\n    Enter 's' for a snake maze \n\t==> ");
				char type = input.nextLine().charAt(0);
				if (type == 'r'|| type == 's' || type == 't') {
					mazeType = type;
				} else throw new Exception();

			} catch (Exception e) {
				System.out.println("Please input a proper value");
			}
		}
		while (mazeSize < 3) {
			try {
				System.out.print("What size maze would you like to build? "
						+ "\nMazes must be at least 3 boxes in width to allow a path through them.  "
						+ "\n\nPlease enter a number from 3 to 10 \n\t==> ");
				mazeSize = input.nextInt();
			} catch (Exception e) {
				System.out.println("Please input a proper value");
			}
		}
		input.close();
		maze = new MazeBoard(mazeSize, mazeType);
		System.out.println(maze);
		maze.dfs(1, 1);
	}
}
