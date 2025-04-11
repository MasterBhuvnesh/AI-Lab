# Lab 7: Graph Coloring Using Constraint Satisfaction

| **Name**       | **Section** | **Roll No.** | **Branch** | **Lab** | **Date**   |
| -------------- | ----------- | ------------ | ---------- | ------- | ---------- |
| Bhuvnesh Verma | A           | 28           | AIML       | AI LAB  | 24/03/2025 |

## Problem Statement

Graph coloring is a classic problem in computer science where the goal is to assign colors to the vertices of a graph such that no two adjacent vertices share the same color. In this lab, we apply a constraint satisfaction approach to solve the graph coloring problem for a map of Australian regions. Each region is represented as a node, and edges represent adjacency between regions. The objective is to assign colors to each region such that no two neighboring regions have the same color.

---

## Algorithm

1. **Initialize**:

   - `assigned`: A dictionary to store the assigned colors for each node (region). Initially, all colors are set to `None`.
   - `neighbors`: A dictionary to define the adjacency list of each node (region).
   - `domain`: A list of available colors (e.g., `['Red', 'Green', 'Blue']`).

2. **Assign Colors**:

   - Iterate through each node in the `assigned` dictionary.
   - For each unassigned node, try assigning a color from the domain.
   - Check if the assigned color violates any constraints (i.e., no adjacent nodes have the same color).
   - If a constraint is violated, try the next color in the domain.
   - If no color satisfies the constraints, backtrack or stop.

3. **Check Constraints**:

   - For a given node, check all its neighbors to ensure none have the same color.
   - If a conflict is found, return `1` (indicating a violation).
   - If no conflicts are found, return `0`.

4. **Output**:

   - Print the assigned color for each node (region).

---

## Code

```python
# Dictionary to store the assigned colors for each node (region).
assigned = {
    'WA': None,  # Western Australia
    'NT': None,  # Northern Territory
    'Q': None,   # Queensland
    'SA': None,  # South Australia
    'NSW': None, # New South Wales
    'V': None,   # Victoria
    'T': None    # Tasmania
}

# Dictionary to define the neighbors of each node (region).
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'Q', 'SA'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Function to assign colors to nodes (regions) while ensuring no adjacent regions have the same color.
def assignCol():
    for key in assigned.keys():
        i, flag = 0, 0
        current = key

        if assigned[key] is None:
            while i <= (len(domain) - 1):
                assigned[current] = domain[i]
                print('The assigned colour for', current, 'is:', assigned[current])

                flag = checkConst(current)

                if flag == 1:
                    i = i + 1
                else:
                    break

# Function to check constraints (e.g., no adjacent regions have the same color)
def checkConst(current):
    for neighbor in neighbors[current]:
        if assigned[neighbor] == assigned[current]:
            return 1
    return 0

# Example domain of colors (e.g., Red, Green, Blue)
domain = ['Red', 'Green', 'Blue']

# Call the function to assign colors
assignCol()
```

---

## Output

```
The assigned colour for WA is: Red
The assigned colour for NT is: Red
The assigned colour for NT is: Green
The assigned colour for Q is: Red
The assigned colour for SA is: Red
The assigned colour for SA is: Green
The assigned colour for SA is: Blue
The assigned colour for NSW is: Red
The assigned colour for NSW is: Green
The assigned colour for V is: Red
The assigned colour for T is: Red
```

---

## Explanation

### Graph Representation

- The graph is represented using two dictionaries:
  - `assigned`: Stores the color assigned to each region.
  - `neighbors`: Defines the adjacency list for each region.

### Color Assignment

- The `assignCol` function iterates through each region and assigns a color from the domain (`['Red', 'Green', 'Blue']`).
- For each region, the function checks if the assigned color conflicts with any of its neighbors using the `checkConst` function.
- If a conflict is found, the function tries the next color in the domain.
- The process continues until all regions are assigned a valid color.

### Constraint Checking

- The `checkConst` function ensures that no two adjacent regions have the same color.
- It iterates through the neighbors of the current region and checks if any neighbor has the same color.
- If a conflict is detected, it returns `1`; otherwise, it returns `0`.

### Execution Steps

1. **WA (Western Australia)**:

   - Assigned color: `Red`.
   - No conflicts with neighbors (`NT` and `SA`).

2. **NT (Northern Territory)**:

   - Initially assigned `Red`, but conflicts with `WA`.
   - Reassigned `Green`.

3. **Q (Queensland)**:

   - Assigned `Red`.
   - No conflicts with neighbors (`NT`, `SA`, `NSW`).

4. **SA (South Australia)**:

   - Initially assigned `Red`, but conflicts with `WA` and `NT`.
   - Reassigned `Green`, but conflicts with `NT`.
   - Reassigned `Blue`.

5. **NSW (New South Wales)**:

   - Initially assigned `Red`, but conflicts with `Q` and `SA`.
   - Reassigned `Green`.

6. **V (Victoria)**:

   - Assigned `Red`.
   - No conflicts with neighbors (`SA`, `NSW`).

7. **T (Tasmania)**:
   - Assigned `Red`.
   - No neighbors, so no conflicts.

---

## Key Points

- Constraint satisfaction is a powerful technique for solving problems like graph coloring.
- The algorithm ensures that no two adjacent regions share the same color by iteratively checking constraints.
- The choice of domain (colors) and the order of assignment can impact the efficiency and outcome of the algorithm.

This implementation successfully solves the graph coloring problem for the given map of Australian regions using a simple constraint satisfaction approach.
