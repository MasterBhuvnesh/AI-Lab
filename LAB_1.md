# Lab 1: Water Jug Problem

| **Name**       | **Section** | **Roll No.** | **Branch** | **Lab** | **Date**   |
| -------------- | ----------- | ------------ | ---------- | ------- | ---------- |
| Bhuvnesh Verma | A           | 28           | AIML       | AI LAB  | 13/01/2025 |

## Problem Statement

The Water Jug Problem is a classic problem in artificial intelligence and computer science. The problem involves two jugs of different capacities and the goal is to measure a specific amount of water using these jugs. The operations allowed are:

1. **Fill a jug** to its full capacity.
2. **Empty a jug** completely.
3. **Pour water from one jug to the other** until either the first jug is empty or the second jug is full.

Given the capacities of the two jugs and a target amount of water, the task is to determine a sequence of steps to measure exactly the target amount of water in one of the jugs.

## Algorithm

The algorithm used to solve the Water Jug Problem in the provided code is as follows:

1. **Initialize**:

   - Set both jugs to be empty.
   - Create an empty list to store the sequence of steps.

2. **Loop until the target is reached**:

   - **Fill Jug 1** if it is empty.
   - **Pour water from Jug 1 to Jug 2** until Jug 2 is full or Jug 1 is empty.
   - **Empty Jug 2** if it is full.
   - **Check** if the target amount of water is in Jug 1. If so, break the loop.

3. **Return** the sequence of steps.

## Code

```python
def func(jug1_capacity, jug2_capacity, target):
    # Initialize variables
    jug1 = 0
    jug2 = 0

    # Store the sequence of steps
    steps = []

    while True:
        # Fill jug1 if it's empty
        if jug1 == 0:
            jug1 = jug1_capacity
            steps.append(f"Fill Jug 1: ({jug1}, {jug2})")

        # Pour from jug1 to jug2
        elif jug2 < jug2_capacity:
            transfer = min(jug1, jug2_capacity - jug2)
            jug1 -= transfer
            jug2 += transfer
            steps.append(f"Pour Jug 1 -> Jug 2: ({jug1}, {jug2})")

        # Empty jug2 if it's full
        elif jug2 == jug2_capacity:
            jug2 = 0
            steps.append(f"Empty Jug 2: ({jug1}, {jug2})")

        # Check if we reached the target
        if jug1 == target :
            steps.append(f"Target reached: ({jug1}, {jug2})")
            break

    return steps


jug1_capacity = 4
jug2_capacity = 3
target = 2

result = func(jug1_capacity, jug2_capacity, target)
for step in result:
    print(step)
```

## Output

The output of the code for the given capacities and target is as follows:

```
Fill Jug 1: (4, 0)
Pour Jug 1 -> Jug 2: (1, 3)
Empty Jug 2: (1, 0)
Pour Jug 1 -> Jug 2: (0, 1)
Fill Jug 1: (4, 1)
Pour Jug 1 -> Jug 2: (2, 3)
Target reached: (2, 3)
```

## Explanation

1. **Fill Jug 1**: Jug 1 is filled to its full capacity (4 liters).
2. **Pour Jug 1 -> Jug 2**: Water is poured from Jug 1 to Jug 2 until Jug 2 is full or Jug 1 is empty. After pouring, Jug 1 has 1 liter and Jug 2 has 3 liters.
3. **Empty Jug 2**: Jug 2 is emptied completely.
4. **Pour Jug 1 -> Jug 2**: The remaining 1 liter from Jug 1 is poured into Jug 2.
5. **Fill Jug 1**: Jug 1 is filled again to its full capacity (4 liters).
6. **Pour Jug 1 -> Jug 2**: Water is poured from Jug 1 to Jug 2 until Jug 2 is full. After pouring, Jug 1 has 2 liters and Jug 2 has 3 liters.
7. **Target reached**: The target of 2 liters in Jug 1 is achieved.

This sequence of steps successfully measures exactly 2 liters of water in Jug 1.

[![Open in Colab](https://img.shields.io/badge/Open%20in%20Colab-%23000000?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/MasterBhuvnesh/AI-Lab/blob/main/labs/LAB_1.ipynb)
