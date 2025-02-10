
import copy

def checkGoal(start, end):
    if start == end:
        return True
    else:
        return False

def misplacedTile(start, end):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if start[i][j] != end[i][j]:
                misplaced += 1
    return misplaced

def manhattanDistance(start, end):
    distance = 0
    for i in range(3):
        for j in range(3):
            if start[i][j] is not None:
                l, m = find(start[i][j], end)
                distance += abs(i-l) + abs(j-m)
    return distance

def find(x, end):
    for i in range(3):
        for j in range(3):
            if x == end[i][j]:
                return i, j
    return -1,-1 # Handle the case where x is not found

def findBlank(currState):
    for i in range(3):
        for j in range(3):
            if currState[i][j] is None:
                return i, j

def genMoves(currState):
    states = []
    k, l = findBlank(currState)

    if k > 0:
        upChild = copy.deepcopy(currState)
        upChild[k][l] = upChild[k-1][l]
        upChild[k-1][l] = None
        states.append(upChild)

    if k < 2:
        downChild = copy.deepcopy(currState)
        downChild[k][l] = downChild[k+1][l]
        downChild[k+1][l] = None
        states.append(downChild)

    if l > 0:
        leftChild = copy.deepcopy(currState)
        leftChild[k][l] = leftChild[k][l-1]
        leftChild[k][l-1] = None
        states.append(leftChild)

    if l < 2:
        rightChild = copy.deepcopy(currState)
        rightChild[k][l] = rightChild[k][l+1]
        rightChild[k][l+1] = None
        states.append(rightChild)

    return states

def childSelection(states, end):
    smallestHeur = float('inf')
    bestState = states[0] if states else None

    for state in states:
        heur = manhattanDistance(state, end)
        if heur < smallestHeur:
            smallestHeur = heur
            bestState = state
    return bestState

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
# start = [[1,3,5],[4,None,2],[6,7,8]]
# end = [[1,3,None], [4,2,5], [6,7,8]]
# hillClimb(start, end, 0, 0)

# start = [[1, 3, 5], [4, None, 2], [6, 7, 8]]
# end = [[1, 3, None], [4, 2, 5], [6, 7, 8]]
# hillClimb(start, end, 0, 0)

start = [[1, 3, 5], [4, None, 2], [6, 7, 8]]
end = [[1, 2, 3], [4, None, 5], [6, 7, 8]]
hillClimb(start, end, 0, 0)
