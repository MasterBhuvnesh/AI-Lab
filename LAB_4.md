# Lab 4: A\* Search Algorithm

| **Name**       | **Section** | **Roll No.** | **Branch** | **Lab** | **Date**   |
| -------------- | ----------- | ------------ | ---------- | ------- | ---------- |
| Bhuvnesh Verma | A           | 28           | AIML       | AI LAB  | 03/01/2025 |

## Problem Statement

A\* Search is an informed search algorithm used to find the shortest path between a start node and a goal node in a weighted graph. It combines the advantages of Uniform Cost Search (UCS) and Greedy Best-First Search by using both the actual cost from the start node and a heuristic estimate of the cost to the goal node. The algorithm prioritizes nodes that minimize the total cost `f(n) = g(n) + h(n)`, where `g(n)` is the cost from the start node to node `n`, and `h(n)` is the heuristic estimate of the cost from node `n` to the goal.

---

## Algorithm

1. **Initialize**:

   - `open_set`: A set to keep track of nodes to be explored, starting with the start node.
   - `closed_set`: A set to keep track of nodes that have already been explored.
   - `g`: A dictionary to store the cost from the start node to each node.
   - `parents`: A dictionary to store the parent of each node for path reconstruction.

2. **Loop until the `open_set` is empty**:

   - Select the node `n` from the `open_set` with the lowest `f(n) = g(n) + h(n)`.
   - If `n` is the goal node, reconstruct and return the path.
   - If `n` is not the goal, explore its neighbors:
     - Calculate the tentative cost `g(m)` for each neighbor `m`.
     - If `m` is not in the `open_set` or `closed_set`, add it to the `open_set` and update its cost and parent.
     - If `m` is already in the `open_set` or `closed_set` and the new cost is lower, update its cost and parent.
   - Move `n` from the `open_set` to the `closed_set`.

3. **Return** the path if the goal is reached, otherwise, indicate that no path exists.

---

## Code

```python
import heapq

# Heuristic function to estimate the cost from node n to the goal
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist[n]

# A* Search Algorithm
def a_star_search(start, goal):
    open_set = set([start])  # Set of nodes to be explored
    closed_set = set()  # Set of nodes already explored
    g = {start: 0}  # Cost from start to each node
    parents = {start: start}  # Parent of each node for path reconstruction

    while len(open_set) > 0:
        n = None
        # Select the node with the lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        # If the goal is reached or no more nodes to explore
        if n == goal or graph2[n] is None:
            pass
        else:
            # Explore neighbors of the current node
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)  # Add to open set
                    parents[m] = n  # Set parent
                    g[m] = g[n] + weight  # Update cost
                    print('+ cost till previous node=', g[n])
                    print('- consolidated cost of', m, 'is', g[m])
                else:
                    # If a better path is found, update cost and parent
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        print('parent of', m, 'is', parents[m])
                        parents[m] = n
                        print(' > parent of', m, 'reinitialized')
                        print('parent of', m, 'is', parents[m])
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        # If no path exists
        if n is None:
            print('Path does not exist!')
            return None

        # If the goal is reached, reconstruct and return the path
        if n == goal:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print('* * * Path found: {} * * *'.format(path))
            return path

        # Move the current node from open_set to closed_set
        open_set.remove(n)
        closed_set.add(n)

    # If no path is found
    print('Path does not exist!')
    return None

# Function to get neighbors of a node
def get_neighbors(v):
    if v in graph2:
        return graph2[v]
    else:
        return None

# Graph representation
graph2 = {
    "A": [('B', 2), ('E', 3)],  # Node A has neighbors B and E with costs 2 and 3
    "B": [('C', 1), ('G', 9)],  # Node B has neighbors C and G with costs 1 and 9
    "C": None,  # Node C has no neighbors
    "D": [('G', 1)],  # Node D has neighbor G with cost 1
    "E": [('D', 6)],  # Node E has neighbor D with cost 6
}

# Perform A* search from node A to node G
a_star_search('A', 'G')
```

---

## Output

```
+ cost till previous node= 0
- consolidated cost of B is 2
+ cost till previous node= 0
- consolidated cost of E is 3
parent of D is E
 > parent of D reinitialized
parent of D is E
+ cost till previous node= 3
- consolidated cost of G is 9
* * * Path found: ['A', 'E', 'D', 'G'] * * *
```

---

## Explanation

### Graph Representation

The graph is represented as a dictionary where each key is a node, and the value is a list of tuples representing the edges. Each tuple contains the neighboring node and the edge cost. For example:

- `"A": [('B', 2), ('E', 3)]` means there is an edge from `A` to `B` with a cost of `2` and an edge from `A` to `E` with a cost of `3`.

### Heuristic Function

The heuristic function `heuristic(n)` provides an estimate of the cost from node `n` to the goal node `G`. This estimate is used to guide the search towards the goal.

### Execution Steps

1. **Start at Node `A`**:

   - Add `A` to the `open_set` with a cost of `0`.
   - Explore neighbors `B` and `E`, updating their costs and parents.

2. **Explore Node `B`**:

   - Add `B` to the `closed_set`.
   - Explore neighbors `C` and `G`, updating their costs and parents.

3. **Explore Node `E`**:

   - Add `E` to the `closed_set`.
   - Explore neighbor `D`, updating its cost and parent.

4. **Explore Node `D`**:

   - Add `D` to the `closed_set`.
   - Explore neighbor `G`, updating its cost and parent.

5. **Reach Goal Node `G`**:
   - Reconstruct the path from `A` to `G` using the `parents` dictionary.
   - The shortest path is `['A', 'E', 'D', 'G']` with a total cost of `9`.

---

## Key Points

- A\* Search is guaranteed to find the shortest path if the heuristic is admissible (never overestimates the cost to the goal).
- The algorithm uses a combination of actual cost (`g(n)`) and heuristic cost (`h(n)`) to prioritize nodes.
- The `open_set` and `closed_set` help manage which nodes to explore and which have already been explored.

This implementation of A\* Search efficiently finds the shortest path from `A` to `G` in the given graph.

[![Open in Colab](https://img.shields.io/badge/Open%20in%20Colab-%23000000?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/MasterBhuvnesh/AI-Lab/blob/main/labs/Lab_4.ipynb)
