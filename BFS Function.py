from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_tree_bfs(root):
    if root is None:
        return 0

    queue = deque([root])
    total = 0

    while queue:
        node = queue.popleft()

        # Add the current node's value to the total
        total += node.value

        # Add left child to queue if it exists
        if node.left:
            queue.append(node.left)

        # Add right child to queue if it exists
        if node.right:
            queue.append(node.right)

    return total


# Example tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print("Sum of all nodes:", sum_tree_bfs(root))