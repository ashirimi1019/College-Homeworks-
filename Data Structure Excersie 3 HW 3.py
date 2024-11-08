class MyLinkListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseLinkList(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Store next node
        current.next = prev  # Reverse current node's pointer
        prev = current  # Move pointers one position ahead
        current = next_node

    return prev

# Helper function to print list for demonstration
def printListing(node):
    while node:
        print(node.value, end=" ")
        node = node.next
    print()

head = MyLinkListNode(5, MyLinkListNode(7, MyLinkListNode(1, MyLinkListNode(2, MyLinkListNode(3)))))
reversed_head = reverseLinkList(head)
printListing(reversed_head)

# Time Complexity: O(n), where n is the number of nodes in the list.
# Space Complexity: O(1), as it uses a constant amount of space.