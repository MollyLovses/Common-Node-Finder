# Finding the Nearest Common Node in a Tree     #
# Module: common_node_finder.py                 #
# Version: 1.0                                  #
# Author: Sergey Patokin                        #
# Last Update: 02.13.2024                       #
# Author URL: https://sergeyforever.online/     #

class TreeNode:
    def __init__(self, val):
        self.val = val  # Initialize the value of the node
        self.left = None  # Initialize the left child node as None
        self.right = None  # Initialize the right child node as None

def find_path(root, target, path):  # Function to find the path from root to a target node
    if root is None:  # Base case: If the root is None, return False
        return False
    
    path.append(root)  # Append the current node to the path
    
    if root == target:  # If the current node is the target node, return True
        return True
    
    # Recursively search for the target node in the left and right subtrees
    if (root.left is not None and find_path(root.left, target, path)) or \
       (root.right is not None and find_path(root.right, target, path)):
        return True

    path.pop()  # If the target node is not found in the subtree, remove the current node from the path
    return False

def find_common_node(root, node1, node2):  # Function to find the nearest common ancestor of two nodes
    # Initialize empty paths for node1 and node2
    path1 = []
    path2 = []

    # Find paths from root to node1 and node2
    if not find_path(root, node1, path1) or not find_path(root, node2, path2):
        return None  # If either node1 or node2 is not found in the tree, return None

    i = 0  # Initialize index for comparing paths
    # Compare paths to find the nearest common ancestor
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:  # If nodes at index i are different, break the loop
            break
        i += 1

    return path1[i - 1] if i > 0 else None  # Return the nearest common ancestor or None if no common ancestor is found

# Example:
# Tree Creating
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
root.right.right.right.right.right = TreeNode(7)

# Nodes A & B
node_A = root.right.right.right.right.right # Set node_A
node_B = root.right.right.left              # Set node_B

# Find the common node
common_node = find_common_node(root, node_A, node_B)  # Find the nearest common ancestor of node_A and node_B

if common_node:  # If a common ancestor is found
    print("The nearest common node:", common_node.val)  # Print the value of the common ancestor
else:  # If no common ancestor is found
    print("The common node was not found.")  # Print a message indicating that no common ancestor was found
