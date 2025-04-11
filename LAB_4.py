# CODE


# Heuristic function to estimate the cost from node n to the goal
def heuristic(n):
    H_dist = {
        "A": 11,
        "B": 6,
        "C": 99,
        "D": 1,
        "E": 7,
        "G": 0,
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
            for m, weight in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)  # Add to open set
                    parents[m] = n  # Set parent
                    g[m] = g[n] + weight  # Update cost
                    print("+ cost till previous node=", g[n])
                    print("- consolidated cost of", m, "is", g[m])
                else:
                    # If a better path is found, update cost and parent
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        print("parent of", m, "is", parents[m])
                        parents[m] = n
                        print(" > parent of", m, "reinitialized")
                        print("parent of", m, "is", parents[m])
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        # If no path exists
        if n is None:
            print("Path does not exist!")
            return None

        # If the goal is reached, reconstruct and return the path
        if n == goal:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print("* * * Path found: {} * * *".format(path))
            return path

        # Move the current node from open_set to closed_set
        open_set.remove(n)
        closed_set.add(n)

    # If no path is found
    print("Path does not exist!")
    return None


# Function to get neighbors of a node
def get_neighbors(v):
    if v in graph2:
        return graph2[v]
    else:
        return None


# Graph representation
graph2 = {
    "A": [("B", 2), ("E", 3)],  # Node A has neighbors B and E with costs 2 and 3
    "B": [("C", 1), ("G", 9)],  # Node B has neighbors C and G with costs 1 and 9
    "C": None,  # Node C has no neighbors
    "D": [("G", 1)],  # Node D has neighbor G with cost 1
    "E": [("D", 6)],  # Node E has neighbor D with cost 6
}

# Perform A* search from node A to node G
a_star_search("A", "G")

# OUTPUT
"""
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
"""

# By - Bhuvnesh Verma
