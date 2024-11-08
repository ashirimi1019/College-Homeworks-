class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    """
    Perform level order traversal on a binary tree.
    
    Args:
    root: TreeNode, the root node of the binary tree.

    Returns:
    A list containing the values of the nodes in level order traversal.

    This function employs a queue to track nodes and their children as it traverses the tree level by level.
    Time Complexity: O(n), where n is the number of nodes in the tree, as each node is visited exactly once.
    Space Complexity: O(n), as the queue may contain all nodes of a level, the maximum of which can be n/2 for a full binary tree.
    """
    # If the root is None, return an empty list.
    if not root:
        return []
    
    # Initialize a queue with the root node.
    queue = [root]
    # This list will store the values of nodes in level order.
    level_order = []
    
    # Loop until the queue is empty.
    while queue:
        # Get the current size of the queue, which represents
        # the number of nodes at the current level.
        level_size = len(queue)
        
        # Iterate over all nodes at the current level.
        for _ in range(level_size):
            # Pop the first node in the queue.
            current_node = queue.pop(0)
            # Append its value to the level order list.
            level_order.append(current_node.val)
            
            # If the current node has a left child, add it to the queue.
            if current_node.left:
                queue.append(current_node.left)
            # If the current node has a right child, add it to the queue.
            if current_node.right:
                queue.append(current_node.right)
                
    return level_order

# Test cases

# Test Case 1: Example tree with balanced nodes.
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print(levelOrderTraversal(root))
# Expected Output: [4, 2, 6, 1, 3, 5, 7]

# Test Case 2: An empty tree.
# root = None
# print(levelOrderTraversal(root))
# Expected Output: []

# Test Case 3: Tree with only left children.
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# print(levelOrderTraversal(root))
# Expected Output: [1, 2, 3]

# Test Case 4: Tree with only right children.
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# print(levelOrderTraversal(root))
# Expected Output: [1, 2, 3]

# Test Case 5: A complete binary tree.
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# print(levelOrderTraversal(root))
# Expected Output: [1, 2, 3, 4, 5, 6, 7]

