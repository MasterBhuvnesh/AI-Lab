# CODE - DFS


# Depth-First Search (DFS) function to traverse a tree
def dfs_tree(tree: dict, start_node: int, end_node: int):
    # Initialize a set to keep track of visited nodes
    visited: set = set()

    # Initialize a list to store the traversal order
    traversal_order: list = []
    # Initialize a queue with the start node
    queue = [(start_node, [start_node])]

    # Continue traversing until the queue is empty
    while queue:
        # Dequeue the next node and its path
        node, path = queue.pop()
        # If the node has not been visited, mark it as visited and add it to the traversal order
        if node not in visited:
            visited.add(node)

            traversal_order.append(node)
            # Print a message to indicate that the node has been visited
            print(f"node {node} visited")
        # If the node is the end node, return the visited nodes and the traversal order
        if node == end_node:
            return visited, traversal_order
        # Add the node's children to the queue if they have not been visited
        for child in tree[node]:
            if child not in visited:
                queue.append((child, path + [child]))
    # Return the visited nodes and the traversal order
    return visited, traversal_order


# CODE DLS


# Depth-Limited Search (DLS) function to traverse a tree
def dls_tree(tree: dict, start_node: int, end_node: int, max_depth: int = 0):
    # Initialize a set to keep track of visited nodes
    visited: set = set()
    # Initialize a list to store the traversal order
    traversal_order: list = []
    # Initialize a queue with the start node and its depth
    queue = [(start_node, [start_node], 0)]

    # Continue traversing until the queue is empty
    while queue:
        # Dequeue the next node, its path, and its depth
        node, path, current_depth = queue.pop()
        # If the current depth exceeds the maximum depth, skip this node
        if current_depth > max_depth:
            continue
        # If the node has not been visited, mark it as visited and add it to the traversal order
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            # Print a message to indicate that the node has been visited
            print(f"node {node} visited")
        # If the node is the end node, return the visited nodes and the traversal order
        if node == end_node:
            return visited, traversal_order
        # Add the node's children to the queue if they have not been visited and are within the maximum depth
        queue.extend(
            [
                (child, path + [child], current_depth + 1)
                for child in tree[node]
                if child not in visited
            ]
        )

    # Return the visited nodes and the traversal order
    return visited, traversal_order


def main():
    # Define a sample tree
    tree: dict = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: [],
    }

    # Perform DFS traversal
    print("DFS Traversal:")
    start_node: int = 1
    end_node: int = 6
    visited, traversal_order = dfs_tree(tree, start_node, end_node)
    print("DFS Traversal Order:", traversal_order)
    print("Visited Order:", traversal_order)

    # Perform DLS traversal
    print("\nDLS Traversal:")
    start_node: int = 1
    end_node: int = 5
    max_depth: int = int(input("Enter the Maximum Depth for the tree: "))
    visited, traversal_order = dls_tree(tree, start_node, end_node, max_depth)
    print("DLS Traversal Order:", traversal_order)
    print("Visited Order:", visited)


if __name__ == "__main__":
    main()

# OUTPUT

# DFS Output

"""
DFS Traversal:
node 1 visited
node 3 visited
node 7 visited
node 6 visited
DFS Traversal Order: [1, 3, 7, 6]
Visited Order: [1, 3, 7, 6]
"""

# DLS Output (Example with `max_depth = 2`)

"""
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
"""

# By - Bhuvnesh Verma
