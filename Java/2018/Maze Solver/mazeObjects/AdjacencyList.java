package mazeObjects;

import java.util.HashMap;

public class AdjacencyList {
	int size;
	Node[] movementPossible;
	HashMap<String,Node[]> adjList;
	
	/*
	 * Create a array of all possible node locations
	 * at every location, reference the node object to find the moveleft move right option
	 * if node object can move left, 
	 */
	class Neighbor {
		Node canMoveTo;
		Neighbor next;
		
		Neighbor(Node move) {
			canMoveTo = move;
			next = null;
		}
	}
	

}
