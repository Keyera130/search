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

def depthFirstSearch(problem: SearchProblem):

    from util import Stack

    # Create a stack to store the frontier (nodes to explore)
    frontier = Stack()
    # Push the start state onto the stack along with an empty list of actions
    frontier.push((problem.getStartState(), []))

    # Keep track of visited nodes to avoid revisiting
    visited = set()

    while not frontier.isEmpty():
        # Pop a state from the stack
        state, actions = frontier.pop()

        # If the state is the goal, return the actions
        if problem.isGoalState(state):
            return actions

        # If this state has not been visited
        if state not in visited:
            visited.add(state)
            # Explore the successors of the current state
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    # Push the successor onto the stack with the new action
                    frontier.push((successor, actions + [action]))

    return []  # Return an empty list if no solution was found


def breadthFirstSearch(problem: SearchProblem):
    from util import Queue

    # Create a queue to store the frontier (nodes to explore)
    frontier = Queue()
    # Push the start state onto the queue along with an empty list of actions
    frontier.push((problem.getStartState(), []))

    # Keep track of visited nodes to avoid revisiting
    visited = set()

    while not frontier.isEmpty():
        # Dequeue a state from the front
        state, actions = frontier.pop()

        # If the state is the goal, return the actions
        if problem.isGoalState(state):
            return actions

        # If this state has not been visited
        if state not in visited:
            visited.add(state)
            # Explore the successors of the current state
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    # Push the successor onto the queue with the new action
                    frontier.push((successor, actions + [action]))

    return []  # Return an empty list if no solution was found


def uniformCostSearch(problem: SearchProblem):
    from util import PriorityQueue

    # Create a priority queue to store the frontier (nodes to explore)
    frontier = PriorityQueue()
    # Push the start state onto the queue with a cost of 0
    frontier.push((problem.getStartState(), [], 0), 0)

    # Keep track of visited nodes to avoid revisiting
    visited = set()

    while not frontier.isEmpty():
        # Pop the state with the least cost
        state, actions, cost = frontier.pop()

        # If the state is the goal, return the actions
        if problem.isGoalState(state):
            return actions

        # If this state has not been visited
        if state not in visited:
            visited.add(state)
            # Explore the successors of the current state
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    totalCost = cost + stepCost
                    # Push the successor onto the queue with the updated cost
                    frontier.push((successor, actions + [action], totalCost), totalCost)

    return []  # Return an empty list if no solution was found


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    from util import PriorityQueue

    # Create a priority queue to store the frontier (nodes to explore)
    frontier = PriorityQueue()
    # Push the start state onto the queue with a cost of 0 and heuristic estimate
    start_cost = heuristic(problem.getStartState(), problem)
    frontier.push((problem.getStartState(), [], 0), start_cost)

    # Keep track of visited nodes to avoid revisiting
    visited = set()

    while not frontier.isEmpty():
        # Pop the state with the lowest f = g + h
        state, actions, cost = frontier.pop()

        # If the state is the goal, return the actions
        if problem.isGoalState(state):
            return actions

        # If this state has not been visited
        if state not in visited:
            visited.add(state)
            # Explore the successors of the current state
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    totalCost = cost + stepCost
                    priority = totalCost + heuristic(successor, problem)
                    # Push the successor onto the queue with the updated cost and heuristic
                    frontier.push((successor, actions + [action], totalCost), priority)

    return []  # Return an empty list if no solution was found



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
