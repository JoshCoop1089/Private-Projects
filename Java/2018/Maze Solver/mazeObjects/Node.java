package mazeObjects;

/*
 * Nodes should contain the data about whether they are a wall, an open space, a visited space,
 *  or a current space, and should also hold edge information about how they link to nodes around them
 *  
 *  This is an object that takes up one space in the array maze, and can also function as a link
 *   in the adjacency lists for running dfs at a later time
 */
public class Node {
	char tileValue;
	boolean visited;
	boolean leftAvailable;
	boolean rightAvailable;
	boolean upAvailable;
	boolean downAvailable;
	Node next;
	
	/*
	 * @param tileValue Plug in '.' for empty, '|' '/' '\' '-' for wall, '*' for visited, and 'X' for currently visiting
	 */
	Node(char tileValue) {
		this.tileValue = tileValue;
	}

	@Override
	public String toString() {
		return Character.toString(tileValue);
	}
}
