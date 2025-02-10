# Lab 3: Uniform Cost Search (UCS)

## Problem Statement

Uniform Cost Search (UCS) is an algorithm used to find the shortest path between a start node and a goal node in a weighted graph. Unlike Depth-First Search (DFS) or Breadth-First Search (BFS), UCS considers the cost of each path and prioritizes exploring the path with the lowest cumulative cost. The goal is to find the path with the minimum total cost from the start node to the goal node.

---

## Algorithm

1. **Initialize**:
   - A set to keep track of visited nodes.
   - A priority queue (implemented as a list) to manage nodes to be explored, sorted by cumulative cost.
   - The priority queue initially contains the start node with a cost of 0.

2. **Loop until the priority queue is empty**:
   - Pop the node with the lowest cumulative cost from the priority queue.
   - If the node is the goal, return the path and its cost.
   - If the node has already been visited, skip it.
   - Mark the node as visited.
   - Explore its neighbors:
     - Calculate the new cumulative cost for each neighbor.
     - Add the neighbor to the priority queue with its updated cost and path.

3. **Return** the path, cost, and list of visited nodes.

---

## Code

```python
import copy

def uniform_cost_search(graph, start, goal):
    visited = set()
    openlist = [(0, [start])]

    while openlist:
        curr_cost, curr_path = openlist.pop(0)
        curr_node = curr_path[-1]

        if curr_node == goal:
            return curr_path, curr_cost, list(visited)

        if curr_node in visited:
            continue

        visited.add(curr_node)

        neighbors = graph[curr_node]
        for edge_cost, neighbor in neighbors:
            if neighbor not in visited:
                new_path = curr_path + [neighbor]
                new_cost = curr_cost + edge_cost

                openlist.append((new_cost, new_path))
                openlist.sort()

    return None, None, list(visited)


graph = {
    'S': [(1, 'A'), (12, 'G')],
    'A': [(3, 'B'), (1, 'C')],
    'B': [(3, 'D')],
    'C': [(1, 'D'), (2, 'G')],
    'D': [(3, 'G')],
    'G': []
}

path, cost, visited = uniform_cost_search(graph, 'S', 'G')
print(f"Path: {path}")
print(f"Cost: {cost}")
print(f"Visited nodes: {visited}")
```

---

## Output

```
Path: ['S', 'A', 'C', 'G']
Cost: 4
Visited nodes: ['S', 'A', 'C', 'B', 'D']
```

---

## Explanation

### Graph Representation
The graph is represented as a dictionary where each key is a node, and the value is a list of tuples representing the edges. Each tuple contains the edge cost and the neighboring node. For example:
- `'S': [(1, 'A'), (12, 'G')]` means there is an edge from `S` to `A` with a cost of `1` and an edge from `S` to `G` with a cost of `12`.

### Execution Steps
1. **Start at Node `S`**:
   - Add `S` to the priority queue with a cost of `0`.
   - Path: `['S']`, Cost: `0`.

2. **Explore Node `S`**:
   - Pop `S` from the queue.
   - Mark `S` as visited.
   - Add its neighbors `A` and `G` to the queue:
     - Path to `A`: `['S', 'A']`, Cost: `1`.
     - Path to `G`: `['S', 'G']`, Cost: `12`.

3. **Explore Node `A`**:
   - Pop `A` from the queue (lowest cost).
   - Mark `A` as visited.
   - Add its neighbors `B` and `C` to the queue:
     - Path to `B`: `['S', 'A', 'B']`, Cost: `4`.
     - Path to `C`: `['S', 'A', 'C']`, Cost: `2`.

4. **Explore Node `C`**:
   - Pop `C` from the queue (lowest cost).
   - Mark `C` as visited.
   - Add its neighbors `D` and `G` to the queue:
     - Path to `D`: `['S', 'A', 'C', 'D']`, Cost: `3`.
     - Path to `G`: `['S', 'A', 'C', 'G']`, Cost: `4`.

5. **Explore Node `B`**:
   - Pop `B` from the queue.
   - Mark `B` as visited.
   - Add its neighbor `D` to the queue:
     - Path to `D`: `['S', 'A', 'B', 'D']`, Cost: `7`.

6. **Explore Node `D`**:
   - Pop `D` from the queue.
   - Mark `D` as visited.
   - Add its neighbor `G` to the queue:
     - Path to `G`: `['S', 'A', 'C', 'D', 'G']`, Cost: `6`.

7. **Explore Node `G`**:
   - Pop `G` from the queue (lowest cost).
   - The goal is reached with the path `['S', 'A', 'C', 'G']` and a total cost of `4`.

---

## Key Points
- UCS guarantees the shortest path in terms of cost for graphs with non-negative edge weights.
- The algorithm uses a priority queue to always explore the least costly path first.
- The visited nodes are tracked to avoid revisiting nodes unnecessarily.

This implementation of UCS efficiently finds the shortest path from `S` to `G` in the given graph.