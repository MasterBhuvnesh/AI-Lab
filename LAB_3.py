# CODE

import copy


# Define a function for uniform cost search
def uniform_cost_search(graph, start, goal):
    # Initialize a set to keep track of visited nodes
    visited = set()
    # Initialize a list to store nodes to be explored, with the starting node as the first node
    openlist = [(0, [start])]

    # Continue exploring nodes until the open list is empty
    while openlist:
        # Get the node with the lowest cost from the open list
        curr_cost, curr_path = openlist.pop(0)
        # Get the current node from the path
        curr_node = curr_path[-1]

        # If the current node is the goal, return the path, cost, and visited nodes
        if curr_node == goal:
            return curr_path, curr_cost, list(visited)

        # If the current node has already been visited, skip it
        if curr_node in visited:
            continue

        # Mark the current node as visited
        visited.add(curr_node)

        # Get the neighbors of the current node
        neighbors = graph[curr_node]
        # Explore each neighbor
        for edge_cost, neighbor in neighbors:
            # If the neighbor has not been visited, create a new path and cost
            if neighbor not in visited:
                new_path = curr_path + [neighbor]
                new_cost = curr_cost + edge_cost

                # Add the new path and cost to the open list and sort it
                openlist.append((new_cost, new_path))
                openlist.sort()

    # If the goal is not reachable, return None
    return None, None, list(visited)


# Define a graph with nodes and their neighbors
graph = {
    "S": [(1, "A"), (12, "G")],  # Node S has neighbors A and G with costs 1 and 12
    "A": [(3, "B"), (1, "C")],  # Node A has neighbors B and C with costs 3 and 1
    "B": [(3, "D")],  # Node B has neighbor D with cost 3
    "C": [(1, "D"), (2, "G")],  # Node C has neighbors D and G with costs 1 and 2
    "D": [(3, "G")],  # Node D has neighbor G with cost 3
    "G": [],  # Node G has no neighbors
}

# Perform uniform cost search on the graph from node S to node G
path, cost, visited = uniform_cost_search(graph, "S", "G")
print(f"Path: {path}")  # Print the shortest path
print(f"Cost: {cost}")  # Print the cost of the shortest path
print(f"Visited nodes: {visited}")  # Print the visited nodes

# OUTPUT

"""
Path: ['S', 'A', 'C', 'G']
Cost: 4
Visited nodes: ['S', 'A', 'C', 'B', 'D']
"""
