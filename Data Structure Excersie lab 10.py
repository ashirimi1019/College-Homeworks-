# ASHIR IMRAN
# 3/24/2024
# DATA STRUCTURE LAB 10
# Definition for a binary tree node provided in the problem statement
class TreeNodes:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def preorder_traversals(root):
    """
    Perform a pre-order traversal of a binary tree and return the result in reversed order.
    Pre-order traversal: Visit the root, then the left subtree, and finally the right subtree.
    
    :param root: TreeNode, the root of the binary tree
    :return: List[int], the values of nodes visited in pre-order, reversed
    """
    if not root:
        return []
    # Perform pre-order traversal and reverse the result before returning
    return [root.val] + preorder_traversals(root.left) + preorder_traversals(root.right)[::-1]

def inorders_traversals(root):
    """
    Perform an in-order traversal of a binary tree and return the result in reversed order.
    In-order traversal: Visit the left subtree, then the root, and finally the right subtree.
    
    :param root: TreeNode, the root of the binary tree
    :return: List[int], the values of nodes visited in in-order, reversed
    """
    if not root:
        return []
    # Perform in-order traversal and reverse the result before returning
    return inorders_traversals(root.left) + [root.val] + inorders_traversals(root.right)[::-1]

def postorders_traversals(root):
    """
    Perform a post-order traversal of a binary tree and return the result in reversed order.
    Post-order traversal: Visit the left subtree, then the right subtree, and finally the root.
    
    :param root: TreeNode, the root of the binary tree
    :return: List[int], the values of nodes visited in post-order, reversed
    """
    if not root:
        return []
    # Perform post-order traversal and reverse the result before returning
    return postorders_traversals(root.left) + postorders_traversals(root.right) + [root.val][::-1]

# Test Cases
# Construct the binary tree as described
root = TreeNodes(4)
root.left = TreeNodes(2)
root.right = TreeNodes(6)
root.left.left = TreeNodes(1)
root.left.right = TreeNodes(3)
root.right.left = TreeNodes(5)
root.right.right = TreeNodes(7)

# Perform Traversals
pre_order_result = preorder_traversals(root)
in_order_result = inorders_traversals(root)
post_order_result = postorders_traversals(root)

# Print results to verify the reverse order
print("Reversed Pre-order Traversal:", pre_order_result)
print("Reversed In-order Traversal:", in_order_result)
print("Reversed Post-order Traversal:", post_order_result)
 