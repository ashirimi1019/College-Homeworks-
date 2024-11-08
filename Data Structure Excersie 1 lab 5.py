#Ashir Imran
# CSc 2720 Lab #N
# Lab time: Wed 3-3:50
# Date: 02/04/2024

def merge_sorting(lst):
    """
    Perform merge sort on the list.
    This function splits the list into halves, sorts each half, and then merges them.
    The sort routine used here is Merge Sort.
    """

    # Check if the list has more than one element
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]  # Split the list into left half
        right_half = lst[mid:]  # Split the list into right half

        # Recursive call to sort each half
        merge_sorting(left_half)
        merge_sorting(right_half)

        # Initialize indices for left_half, right_half, and the merged list
        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in the left_half
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in the right_half
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

def deduplication(lst):
    """
    Remove duplicates from the sorted list in O(n) time and O(1) space complexity.
    This function assumes that the input list is already sorted.
    """

    # Check if the list is empty
    if not lst:
        return []

    # Initialize a new index to store the position of unique elements
    index = 0

    # Iterate through the list starting from the second element
    for i in range(1, len(lst)):
        # Check if the current element is different from the previous one
        if lst[i] != lst[index]:
            index += 1
            lst[index] = lst[i]

    # Slice the list to include only unique elements
    return lst[:index + 1]

# Example usage
LST = [50, 11, 33, 21, 40, 50, 40, 40, 21]
merge_sorting(LST)  # Sort the list using merge sort
LST = deduplication(LST)  # De-duplicate the sorted list
print(LST)

# Test cases:
# 1. If the input is None or an empty list, the function should return an empty list.
# 2. When the input list contains only one element, the function should return the same list since there are no duplicates to remove.
# 3. In the scenario where all elements in the input list are identical, the function should return a list with just one instance of that element.
# 4. Given the input list is already sorted, the function should remove duplicates while preserving the order.
# 5. In cases where the input list includes negative numbers and zeros, the function should handle them appropriately, returning a sorted and de-duplicated list.
