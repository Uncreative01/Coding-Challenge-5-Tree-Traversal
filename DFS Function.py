class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_tree_dfs(node):
    if node is None:
        return 0

    # Add current node's value
    total = node.value

    # Recursively add left and right subtrees
    total += sum_tree_dfs(node.left)
    total += sum_tree_dfs(node.right)

    return total

# Example tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print("Sum of all nodes (DFS):", sum_tree_dfs(root))