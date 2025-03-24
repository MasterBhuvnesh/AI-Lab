# Lab 6: Minimax Algorithm for Decision Making in Game Trees

## Problem Statement

The Minimax algorithm is a decision-making algorithm used in two-player games, such as chess or tic-tac-toe, to determine the optimal move for a player. The algorithm assumes that the opponent is also playing optimally. It recursively evaluates all possible moves and chooses the move that maximizes the player's advantage while minimizing the opponent's advantage. In this lab, we implement the Minimax algorithm to find the optimal value in a game tree represented by a list of scores at the leaf nodes.

---

## Algorithm

1. **Initialize**:

   - `scores`: A list of scores at the leaf nodes of the game tree.
   - `tree_depth`: The depth of the game tree, calculated as `log2(len(scores))`.

2. **Minimax Function**:

   - **Base Case**: If the current depth equals the target depth, return the score of the current node.
   - **Maximizer's Turn**: If it's the maximizer's turn, recursively compute the values of the left and right children and return the maximum of the two.
   - **Minimizer's Turn**: If it's the minimizer's turn, recursively compute the values of the left and right children and return the minimum of the two.

3. **Output**:

   - Print the minimax value at each step.
   - Print the optimal value at the end.

---

## Code

```python
import math

def minimax(current_depth, node_index, is_max_turn, scores, target_depth):
    """
    Recursively computes the minimax value for a given node in a game tree.

    :param current_depth: Current depth in the game tree.
    :param node_index: Index of the current node in the tree.
    :param is_max_turn: Boolean indicating whether it's the maximizer's turn.
    :param scores: List of scores at the leaf nodes of the tree.
    :param target_depth: The maximum depth to search in the tree.
    :return: The minimax value of the current node.
    """
    # Base case: if target depth is reached, return the score of the current node
    if current_depth == target_depth:
        print(f"minimax value is: {scores[node_index]}")
        return scores[node_index]

    if is_max_turn:
        # Maximizer's turn: choose the maximum value between the two children
        left_value = minimax(current_depth + 1, node_index * 2, False, scores, target_depth)
        right_value = minimax(current_depth + 1, node_index * 2 + 1, False, scores, target_depth)
        max_value = max(left_value, right_value)
        print(f"Max value selected is= {max_value}")
        return max_value
    else:
        # Minimizer's turn: choose the minimum value between the two children
        left_value = minimax(current_depth + 1, node_index * 2, True, scores, target_depth)
        right_value = minimax(current_depth + 1, node_index * 2 + 1, True, scores, target_depth)
        min_value = min(left_value, right_value)
        print(f"Min value selected is= {min_value}")
        return min_value

def main():
    # List of scores at the leaf nodes of the game tree
    scores = [10, 2, 12, 16, 2, 7, -5, -80]

    # Calculate the depth of the tree based on the number of scores
    tree_depth = int(math.log(len(scores), 2))

    # Compute the optimal value using the minimax algorithm
    optimal_value = minimax(0, 0, False, scores, tree_depth)

    # Print the optimal value
    print("\n--------------------------------------\n")
    print(f"The optimal value is {optimal_value}")

if __name__ == "__main__":
    main()
```

---

## Output

```
minimax value is: 10
minimax value is: 2
Min value selected is= 2
minimax value is: 12
minimax value is: 16
Min value selected is= 12
Max value selected is= 12
minimax value is: 2
minimax value is: 7
Min value selected is= 2
minimax value is: -5
minimax value is: -80
Min value selected is= -80
Max value selected is= 2
Min value selected is= 2

--------------------------------------

The optimal value is 2
```

---

## Explanation

### Game Tree Representation

- The game tree is represented by a list of scores at the leaf nodes: `[10, 2, 12, 16, 2, 7, -5, -80]`.
- The depth of the tree is calculated as `log2(len(scores))`, which is `3` for this example.

### Minimax Algorithm

1. **Base Case**:

   - When the current depth equals the target depth, the algorithm returns the score of the current node.

2. **Maximizer's Turn**:

   - The algorithm recursively computes the values of the left and right children and selects the maximum value.

3. **Minimizer's Turn**:
   - The algorithm recursively computes the values of the left and right children and selects the minimum value.

### Execution Steps

1. **Leaf Nodes**:

   - The algorithm reaches the leaf nodes and prints their values: `10, 2, 12, 16, 2, 7, -5, -80`.

2. **Minimizer's Turn**:

   - At depth `2`, the minimizer selects the minimum values from the leaf nodes:
     - `min(10, 2) = 2`
     - `min(12, 16) = 12`
     - `min(2, 7) = 2`
     - `min(-5, -80) = -80`

3. **Maximizer's Turn**:

   - At depth `1`, the maximizer selects the maximum values from the minimizer's results:
     - `max(2, 12) = 12`
     - `max(2, -80) = 2`

4. **Final Minimizer's Turn**:

   - At depth `0`, the minimizer selects the minimum value from the maximizer's results:
     - `min(12, 2) = 2`

5. **Optimal Value**:
   - The optimal value is `2`, which is printed as the final result.

---

## Key Points

- The Minimax algorithm is used to determine the optimal move in two-player games.
- It assumes that the opponent is also playing optimally.
- The algorithm alternates between maximizing and minimizing the possible outcomes at each level of the game tree.
- The optimal value represents the best possible outcome for the player, assuming the opponent plays optimally.

This implementation of the Minimax algorithm successfully computes the optimal value for the given game tree.
