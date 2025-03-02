# CODE

import copy

# Initial state and goal state for the puzzle
start = [[1, 3, 5], [4, None, 2], [6, 7, 8]]
goal = [[1, 3, None], [4, 2, 5], [6, 7, 8]]

# Function to find the position of the empty tile (None)
def empty_tile(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] is None:
                return [i, j]

# Function to count the number of misplaced tiles compared to the goal state
def misplace(start, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if start[i][j] != goal[i][j]:
                count += 1
    return count

# Function to move the empty tile up
def move_up(start, goal):
    arr = copy.deepcopy(start)
    x, y = empty_tile(arr)
    if x > 0:
        arr[x][y], arr[x-1][y] = arr[x-1][y], arr[x][y]
        return (arr, misplace(arr, goal))
    return None

# Function to move the empty tile down
def move_down(start, goal):
    arr = copy.deepcopy(start)
    x, y = empty_tile(arr)
    if x < 2:
        arr[x][y], arr[x+1][y] = arr[x+1][y], arr[x][y]
        return (arr, misplace(arr, goal))
    return None

# Function to move the empty tile left
def move_left(start, goal):
    arr = copy.deepcopy(start)
    x, y = empty_tile(arr)
    if y > 0:
        arr[x][y], arr[x][y-1] = arr[x][y-1], arr[x][y]
        return (arr, misplace(arr, goal))
    return None

# Function to move the empty tile right
def move_right(start, goal):
    arr = copy.deepcopy(start)
    x, y = empty_tile(arr)
    if y < 2:
        arr[x][y], arr[x][y+1] = arr[x][y+1], arr[x][y]
        return (arr, misplace(arr, goal))
    return None

# Hill Climbing algorithm to solve the puzzle
def hill_climbing(start, goal):
    current_state = copy.deepcopy(start)
    current_h = misplace(current_state, goal)
    steps = 0
    all_states = []

    print("Initial state:")
    for row in current_state:
        print(row)
    print(f"Initial h(n): {current_h}\n")

    while True:
        steps += 1
        print(f"Step {steps}: - ")

        # Generate all possible neighboring states
        neighbors = [
            move_up(current_state, goal),
            move_down(current_state, goal),
            move_left(current_state, goal),
            move_right(current_state, goal)
        ]
        stack = [ ] 
        # Filter out None values (invalid moves)
        neighbors = [neighbor for neighbor in neighbors if neighbor is not None]

        # Print all possible states
        print("\n ------------------ \n")
        print("Possible states:")
        for i, neighbor in enumerate(neighbors):
            state, h = neighbor
            print(f"State {i + 1}:")
            for row in state:
                print(row)
            print(f"h(n): {h}\n")

        # Find the neighbor with the lowest h(n)
        best_neighbor = None
        best_h = current_h
        for neighbor in neighbors:
            state, h = neighbor
            if h < best_h:
                best_neighbor = state
                best_h = h

        # If no better neighbor is found, stop
        if best_h >= current_h:
            print("No better neighbor found. Stopping.")
            break

        # Move to the best neighbor
        current_state = best_neighbor
        current_h = best_h
        all_states.append(current_state)

        # Print the selected state and h(n)
        print("\n ------------------ \n")
        print("Selected state:")
        for row in current_state:
            print(row)
        print(f"h(n): {current_h}\n")
        print("\n ------------------ \n")

        # Check if the goal state is reached
        if current_h == 0:
            print("Goal state reached!")
            break

    print(f"Total steps taken: {steps}")

    # Print all states
    print("\nAll states:")
    for step, state in enumerate(all_states, start=1):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()

# Run the hill climbing algorithm
hill_climbing(start, goal)

# OUTPUT

'''
Initial state:
[1, 3, 5]
[4, None, 2]
[6, 7, 8]
Initial h(n): 3

Step 1: - 

 ------------------ 

Possible states:
State 1:
[1, None, 5]
[4, 3, 2]
[6, 7, 8]
h(n): 4

State 2:
[1, 3, 5]
[4, 7, 2]
[6, None, 8]
h(n): 4

State 3:
[1, 3, 5]
[None, 4, 2]
[6, 7, 8]
h(n): 4

State 4:
[1, 3, 5]
[4, 2, None]
[6, 7, 8]
h(n): 2


 ------------------ 

Selected state:
[1, 3, 5]
[4, 2, None]
[6, 7, 8]
h(n): 2


 ------------------ 

Step 2: - 

 ------------------ 

Possible states:
State 1:
[1, 3, None]
[4, 2, 5]
[6, 7, 8]
h(n): 0

State 2:
[1, 3, 5]
[4, 2, 8]
[6, 7, None]
h(n): 3

State 3:
[1, 3, 5]
[4, None, 2]
[6, 7, 8]
h(n): 3


 ------------------

Selected state:
[1, 3, None]
[4, 2, 5]
[6, 7, 8]
h(n): 0


 ------------------

Goal state reached!
Total steps taken: 2

All states:
Step 1:
[1, 3, 5]
[4, 2, None]
[6, 7, 8]

Step 2:
[1, 3, None]
[4, 2, 5]
[6, 7, 8]
'''