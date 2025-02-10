# CODE 

def func(jug1_capacity :int , jug2_capacity : int, target : int) -> int:
    # Initialize variables to track the current state of the jugs
    jug1 = 0
    jug2 = 0

    # Store the sequence of steps to reach the target
    steps = []

    # Continue the process until the target is reached
    while True:
        # Fill jug1 if it's empty
        if jug1 == 0:
            jug1 = jug1_capacity
            steps.append(f"Fill Jug 1: ({jug1}, {jug2})")

        # Pour from jug1 to jug2 if jug2 is not full
        elif jug2 < jug2_capacity:
            # Calculate the amount to transfer
            transfer = min(jug1, jug2_capacity - jug2)
            jug1 -= transfer
            jug2 += transfer
            steps.append(f"Pour Jug 1 -> Jug 2: ({jug1}, {jug2})")

        # Empty jug2 if it's full
        elif jug2 == jug2_capacity:
            jug2 = 0
            steps.append(f"Empty Jug 2: ({jug1}, {jug2})")

        # Check if we reached the target
        if jug1 == target:
            steps.append(f"Target reached: ({jug1}, {jug2})")
            break

    # Return the sequence of steps
    return steps


# Define the capacities of the jugs and the target
jug1_capacity = 4
jug2_capacity = 3
target = 2

# Call the function to get the sequence of steps
result = func(jug1_capacity, jug2_capacity, target)

# Print the sequence of steps
for step in result:
    print(step)

# OUTPUT 

'''
Fill Jug 1: (4, 0)
Pour Jug 1 -> Jug 2: (1, 3)
Empty Jug 2: (1, 0)
Pour Jug 1 -> Jug 2: (0, 1)
Fill Jug 1: (4, 1)
Pour Jug 1 -> Jug 2: (2, 3)
Target reached: (2, 3)
'''