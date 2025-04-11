# CODE

import math


def minimax(current_depth, node_index, is_max_turn, scores, target_depth):

    # Base case: if target depth is reached, return the score of the current node
    if current_depth == target_depth:
        print(f"minimax value is: {scores[node_index]}")
        return scores[node_index]

    if is_max_turn:
        # Maximizer's turn: choose the maximum value between the two children
        left_value = minimax(
            current_depth + 1, node_index * 2, False, scores, target_depth
        )
        right_value = minimax(
            current_depth + 1, node_index * 2 + 1, False, scores, target_depth
        )
        max_value = max(left_value, right_value)
        print(f"Max value selected is= {max_value}")
        return max_value
    else:
        # Minimizer's turn: choose the minimum value between the two children
        left_value = minimax(
            current_depth + 1, node_index * 2, True, scores, target_depth
        )
        right_value = minimax(
            current_depth + 1, node_index * 2 + 1, True, scores, target_depth
        )
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

# OUTPUT

"""
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
"""

# By - Bhuvnesh Verma
