# Ashir Imran
# LAB 7
# 2/25/2024
class Noding:
    def __init__(self, data):
        # Initialize a node with provided data
        self.data = data
        self.next = None

class LinkedListing:
    def __init__(self):
        # Initialize a linked list with no head node
        self.head = None

    def appendix(self, data):
        # Append a new node with provided data to the end of the linked list
        new_node = Noding(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_listing(self):
        # Print the elements of the linked list
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            if current_node.next:
                print("->", end=" ")
            current_node = current_node.next
        print()

    def delete_dnth_from_end(self, n):
        # Delete the nth node from the end of the linked list
        dummy = Noding(0)
        dummy.next = self.head
        fast = slow = dummy

        for _ in range(n + 1):
            if not fast:  # Ensure we don't call .next on None
                return
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        if slow.next:  # Ensure slow.next is not None before accessing slow.next.next
            slow.next = slow.next.next
        self.head = dummy.next

# Create and populate the linked list
ll = LinkedListing()
for value in [50, 11, 33, 21, 40, 71]:
    ll.appendix(value)

# Print the original list
print("Original List:")
ll.print_listing()

# Delete the 2nd node from the end
ll.delete_dnth_from_end(2)

# Print the modified list
print("After Deleting 2nd Node from End:")
ll.print_listing()
