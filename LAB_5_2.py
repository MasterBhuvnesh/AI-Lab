# CODE

import copy


# Check if the start state is the same as the end state
def checkGoal(start, end):
    if start == end:
        return True
    else:
        return False


# Calculate the number of misplaced tiles between the start and end states
def misplacedTile(start, end):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if start[i][j] != end[i][j]:
                misplaced += 1
    return misplaced


# Calculate the Manhattan distance between the start and end states
def manhattanDistance(start, end):
    distance = 0
    for i in range(3):
        for j in range(3):
            if start[i][j] is not None:
                l, m = find(start[i][j], end)
                distance += abs(i - l) + abs(j - m)
    return distance


# Find the position of a tile in the end state
def find(x, end):
    for i in range(3):
        for j in range(3):

            if x == end[i][j]:
                return i, j
    return -1, -1  # Handle the case where x is not found


# Find the position of the blank (None) tile in the current state
def findBlank(currState):
    for i in range(3):
        for j in range(3):
            if currState[i][j] is None:
                return i, j


# Generate all possible moves from the current state
def genMoves(currState):
    states = []
    k, l = findBlank(currState)

    # Move the blank tile up
    if k > 0:
        upChild = copy.deepcopy(currState)
        upChild[k][l] = upChild[k - 1][l]
        upChild[k - 1][l] = None
        states.append(upChild)

    # Move the blank tile down
    if k < 2:
        downChild = copy.deepcopy(currState)
        downChild[k][l] = downChild[k + 1][l]
        downChild[k + 1][l] = None
        states.append(downChild)

    # Move the blank tile left
    if l > 0:
        leftChild = copy.deepcopy(currState)
        leftChild[k][l] = leftChild[k][l - 1]
        leftChild[k][l - 1] = None
        states.append(leftChild)

    # Move the blank tile right
    if l < 2:
        rightChild = copy.deepcopy(currState)
        rightChild[k][l] = rightChild[k][l + 1]
        rightChild[k][l + 1] = None
        states.append(rightChild)

    return states


# Select the best child state based on the Manhattan distance heuristic
def childSelection(states, end):
    smallestHeur = float("inf")
    bestState = states[0] if states else None

    for state in states:
        heur = manhattanDistance(state, end)
        if heur < smallestHeur:
            smallestHeur = heur
            bestState = state
    return bestState


# Perform the hill climbing algorithm to solve the puzzle
def hillClimb(start, end, depth, iter):
    iter += 1
    if iter > 5:
        print("No solution found in desired iteration")
        return -1
    print()
    print("Iteration:", iter)
    print("Start:", start)
    print("Depth:", depth)
    if checkGoal(start, end):
        print("Goal reached")
        return depth
    else:
        states = genMoves(start)
        bestState = childSelection(states, end)
        depth += 1
        if bestState is None:
            print("No solution found ")
            return -1
        return hillClimb(bestState, end, depth, iter)


# Test cases

# Case 1

# start = [[1,3,5],[4,None,2],[6,7,8]]
# end = [[1,3,None], [4,2,5], [6,7,8]]
# hillClimb(start, end, 0, 0)

# Case 2

# start = [[1, 3, 5], [4, None, 2], [6, 7, 8]]
# end = [[1, 3, None], [4, 2, 5], [6, 7, 8]]
# hillClimb(start, end, 0, 0)

# Case 3

start = [[1, 3, 5], [4, None, 2], [6, 7, 8]]
end = [[1, 2, 3], [4, None, 5], [6, 7, 8]]
hillClimb(start, end, 0, 0)

#  OUTPUT

"""

# CASE 1 :

Iteration: 1
Start: [[1, 3, 5], [4, None, 2], [6, 7, 8]]
Depth: 0

Iteration: 2
Start: [[1, 3, 5], [4, 2, None], [6, 7, 8]]
Depth: 1

Iteration: 3
Start: [[1, 3, None], [4, 2, 5], [6, 7, 8]]
Depth: 2
Goal reached

# CASE 2 :

Iteration: 1
Start: [[1, 3, 5], [4, None, 2], [6, 7, 8]]
Depth: 0

Iteration: 2
Start: [[1, 3, 5], [4, 2, None], [6, 7, 8]]
Depth: 1

Iteration: 3
Start: [[1, 3, None], [4, 2, 5], [6, 7, 8]]
Depth: 2
Goal reached

# CASE 3 : 

Iteration: 1
Start: [[1, 3, 5], [4, None, 2], [6, 7, 8]]
Depth: 0

Iteration: 2
Start: [[1, 3, 5], [4, 2, None], [6, 7, 8]]
Depth: 1

Iteration: 3
Start: [[1, 3, None], [4, 2, 5], [6, 7, 8]]
Depth: 2

Iteration: 4
Start: [[1, None, 3], [4, 2, 5], [6, 7, 8]]
Depth: 3

Iteration: 5
Start: [[1, 2, 3], [4, None, 5], [6, 7, 8]]
Depth: 4
Goal reached

"""

# By - Bhuvnesh Verma
