# Nearest Common Ancestor Finder

This Python script allows you to find the nearest common ancestor of two nodes in a binary tree.

## Overview

The code consists of a TreeNode class representing nodes in the binary tree and two functions:

1. find_path: This function finds the path from the root to a target node in the tree using depth-first search (DFS).
2. find_common_node: This function finds the nearest common ancestor of two nodes by comparing their paths from the root.

## Usage

To use the code, follow these steps:

1. Define the binary tree by creating TreeNode objects and connecting them appropriately.
2. Set the nodes for which you want to find the nearest common ancestor.
3. Call the find_common_node function with the root of the tree and the two nodes as arguments.
4. Check if a common ancestor is found and print its value if it exists.

Example:

`python
# Define the binary tree
root = TreeNode(1)
root.right = TreeNode(2)
# Add more nodes as needed...

# Set nodes A and B
node_A = root.right.right.right.right.right
node_B = root.right.right.left

# Find the nearest common ancestor
common_node = find_common_node(root, node_A, node_B)

# Print the result
if common_node:
    print("The nearest common node:", common_node.val)
else:
    print("The common node was not found.")
