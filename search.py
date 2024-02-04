# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def search(problem, mode, heuirstic):
    if mode == "dfs":
        work_list = util.Stack()
    elif mode == "bfs":
        work_list = util.Queue()
    elif mode == "ucs" or mode == "astar":
	work_list = util.PriorityQueue()
    else:
	return None

    start_node = problem.getStartState()
    # check if we are already at the goal.
    if problem.isGoalState(start_node):
        return []
	

    if mode == "bfs" or mode == "dfs":
    	start_node_and_path = (start_node, [])
    	work_list.push(start_node_and_path)
    else:
	start_node_cost = 0 
	start_node_priority = 0
	start_node_and_path_with_cost = (start_node, [], 0)
	work_list.push(start_node_and_path_with_cost, start_node_priority)

    # Lookup set for retrieving visited_nodes in O(1) time complexity.
    visited_set = {}
    while not(work_list.isEmpty()):
	if mode == "bfs" or mode == "dfs":
            curr_node, path_to_curr_node = work_list.pop()
        else:
            curr_node, path_to_curr_node, curr_cost = work_list.pop()

	# uses o(1) lookup by hashing it as visited_set is a python dict.
	if curr_node in visited_set:
            continue

	# mark this node as visited
	visited_set[curr_node] = True

        if problem.isGoalState(curr_node):
            return path_to_curr_node

        # relative_path_to_next_node is how to get to next node from curr_node.
        for next_node, relative_path_to_next_node, cost in problem.getSuccessors(curr_node):
            path_to_next_node = path_to_curr_node + [relative_path_to_next_node]
	    if mode == "bfs" or mode == "dfs":
                next_node_and_path = (next_node, path_to_next_node)
            	work_list.push(next_node_and_path)
            else:
		next_node_cost = curr_cost + cost
                next_node_and_path_and_cost =  (next_node, path_to_next_node, next_node_cost)
		if mode == "ucs":
		    # if mode is ucs, cost is uniform and the priority is the cost. 
            	    work_list.push(next_node_and_path_and_cost, next_node_cost)
		else:
		    # if we are doing astar, we will have a cost function which will change priority
		    next_node_priority = next_node_cost + heuirstic(next_node, problem)
            	    work_list.push(next_node_and_path_and_cost, next_node_priority)
  		    
    return None

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    result = search(problem, "dfs", None)
    if result != None:
        return result
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Since this is a DFS we are using a stack.
    result = search(problem, "bfs", None)
    if result != None:
        return result
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    result = search(problem, "ucs", None)
    if result != None:
        return result
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    result = search(problem, "astar", heuristic)
    if result != None:
	return result
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
