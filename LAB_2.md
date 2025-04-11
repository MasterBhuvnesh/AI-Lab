# Lab 2: Depth-First Search (DFS) and Depth-Limited Search (DLS)

| **Name**       | **Section** | **Roll No.** | **Branch** | **Lab** | **Date**   |
| -------------- | ----------- | ------------ | ---------- | ------- | ---------- |
| Bhuvnesh Verma | A           | 28           | AIML       | AI LAB  | 20/01/2025 |

## Problem Statement

The Depth-First Search (DFS) and Depth-Limited Search (DLS) algorithms are fundamental graph traversal techniques used in computer science. The goal is to explore a graph or tree structure by visiting nodes in a systematic manner.

- **DFS** explores as far as possible along each branch before backtracking.
- **DLS** is a variant of DFS that limits the depth of exploration to a specified maximum depth.

Given a tree structure and a target node, the task is to traverse the tree using DFS and DLS and find the traversal order and visited nodes.

---

## Algorithm

### Depth-First Search (DFS)

1. **Initialize**:

   - A set to keep track of visited nodes.
   - A list to store the traversal order.
   - A stack (implemented as a list) to manage the nodes to be explored.

2. **Loop until the stack is empty**:

   - Pop a node from the stack.
   - If the node is not visited:
     - Mark it as visited.
     - Add it to the traversal order.
     - Push its unvisited children onto the stack.

3. **Return** the visited nodes and traversal order.

### Depth-Limited Search (DLS)

1. **Initialize**:

   - A set to keep track of visited nodes.
   - A list to store the traversal order.
   - A stack (implemented as a list) to manage the nodes to be explored, along with their current depth.

2. **Loop until the stack is empty**:

   - Pop a node, its path, and its current depth from the stack.
   - If the current depth exceeds the maximum depth, skip the node.
   - If the node is not visited:
     - Mark it as visited.
     - Add it to the traversal order.
     - Push its unvisited children onto the stack with their updated depth.

3. **Return** the visited nodes and traversal order.

---

## Code

```python
def dfs_tree(tree: dict, start_node: int, end_node: int):
    visited: set = set()
    traversal_order: list = []
    queue = [(start_node, [start_node])]

    while queue:
        node, path = queue.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            print(f"node {node} visited")
        if node == end_node:
            return visited, traversal_order
        for child in tree[node]:
            if child not in visited:
                queue.append((child, path + [child]))
    return visited, traversal_order


def dls_tree(tree: dict, start_node: int, end_node: int, max_depth: int = 0):
    visited: set = set()
    traversal_order: list = []
    queue = [(start_node, [start_node], 0)]

    while queue:
        node, path, current_depth = queue.pop()
        if current_depth > max_depth:
            continue
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            print(f"node {node} visited")
        if node == end_node:
            return visited, traversal_order
        queue.extend([(child, path + [child], current_depth + 1) for child in tree[node] if child not in visited])

    return visited, traversal_order


def main():
    tree: dict = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: [],
    }

    print("DFS Traversal:")
    start_node: int = 1
    end_node: int = 6
    visited, traversal_order = dfs_tree(tree, start_node, end_node)
    print("DFS Traversal Order:", traversal_order)
    print("Visited Order:", traversal_order)

    print("\nDLS Traversal:")
    start_node: int = 1
    end_node: int = 5
    max_depth: int = int(input("Enter the Maximum Depth for the tree: "))
    visited, traversal_order = dls_tree(tree, start_node, end_node, max_depth)
    print("DLS Traversal Order:", traversal_order)
    print("Visited Order:", visited)


if __name__ == "__main__":
    main()
```

---

## Output

### DFS Output

```
DFS Traversal:
node 1 visited
node 3 visited
node 7 visited
node 6 visited
DFS Traversal Order: [1, 3, 7, 6]
Visited Order: [1, 3, 7, 6]
```

### DLS Output (Example with `max_depth = 2`)

```
DLS Traversal:
Enter the Maximum Depth for the tree: 2
node 1 visited
node 3 visited
node 7 visited
node 6 visited
node 2 visited
node 5 visited
DLS Traversal Order: [1, 3, 7, 6, 2, 5]
Visited Order: {1, 2, 3, 5, 6, 7}
```

---

## Explanation

### DFS Explanation

1. **Start at Node 1**: Mark it as visited and add it to the traversal order.
2. **Explore Node 3**: Since DFS prioritizes deeper exploration, Node 3 is visited next.
3. **Explore Node 7**: Node 7 is visited as it is a child of Node 3.
4. **Explore Node 6**: Node 6 is visited as it is the next child of Node 3.
5. **Target Node 6 is found**: The traversal stops.

### DLS Explanation (with `max_depth = 2`)

1. **Start at Node 1**: Mark it as visited and add it to the traversal order.
2. **Explore Node 3**: Node 3 is visited as it is within the depth limit.
3. **Explore Node 7**: Node 7 is visited as it is within the depth limit.
4. **Explore Node 6**: Node 6 is visited as it is within the depth limit.
5. **Backtrack to Node 2**: Node 2 is visited as it is within the depth limit.
6. **Explore Node 5**: Node 5 is visited as it is within the depth limit.
7. **Target Node 5 is found**: The traversal stops.

Both algorithms successfully traverse the tree and find the target node while adhering to their respective constraints. The `main()` function organizes the execution of both DFS and DLS, making the code modular and easy to use.

[![Open in Colab](https://img.shields.io/badge/Open%20in%20Colab-%23000000?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/MasterBhuvnesh/AI-Lab/blob/main/labs/Lab_2.ipynb)
