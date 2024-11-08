class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def delete_node(root, val):
    if root is None:
        return None
    if val < root.val:
        root.left = delete_node(root.left, val)
    elif val > root.val:
        root.right = delete_node(root.right, val)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # Node with two children: get the in-order successor
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)
    return root

# Function to delete the root of the BST
def delete_root(root):
    if root is None:
        return None
    if root.right is None:
        return root.left
    else:
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, root.val)
    return root

# Function for in-order traversal of the BST
def inorder_traversal(root):
    result = []
    def inorder(node):
        if node is not None:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    inorder(root)
    return result

def test_delete_root():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root = delete_root(root)
    expected_output = [1, 2, 3, 5, 6, 7]
    assert inorder_traversal(root) == expected_output, f"Expected: {expected_output}, Got: {inorder_traversal(root)}"

if __name__ == "__main__":
    # Run the test case
    test_delete_root()
    print("Test case passed.")
