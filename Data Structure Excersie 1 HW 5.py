# Ashir Imran
# CSc 2720 Homework #5
# Due time: 04/23/2024

def is_BSTL_util(arr, index, low, high):
    # Base case: if index is greater than the number of nodes, return True
    if index >= len(arr):
        return True

    # If the current node's value is out of the allowed range, return False
    if arr[index] < low or arr[index] > high:
        return False

    # Recursively check the left and right subtrees with updated ranges
    # Left subtree's values should be between low and current node's value
    # Right subtree's values should be between current node's value and high
    return (is_BSTL_util(arr, 2 * index + 1, low, arr[index] - 1) and
            is_BSTL_util(arr, 2 * index + 2, arr[index] + 1, high))

def is_BSTL(arr):
    # Call the utility function starting with the whole range of integer values
    return is_BSTL_util(arr, 0, float('-inf'), float('inf'))

# Example usage:
arr = [10, 5, 15, 2, 7, 11, 25, 1]
print(is_BSTL(arr))  # Output should be True