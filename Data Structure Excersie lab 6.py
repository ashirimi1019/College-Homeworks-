# Ashir Imran
# CSC 2720 Lab 6
# Due time: 02/18/2024
# Quick Sort Algorithm
def quick_sorting(arr, low, high):
    """
    Recursively sorts a list of integers using the Quick Sort algorithm.
    """
    if low < high:
        # Partition the array and obtain the pivot index
        pi = partitioning(arr, low, high)

        # Recursively sort elements before and after the partition
        quick_sorting(arr, low, pi - 1)
        quick_sorting(arr, pi + 1, high)

# Partitioning Function
def partitioning(arr, low, high):
    """
    Partitions the array into elements less than the pivot, the pivot itself,
    and elements greater than the pivot. Returns the index of the pivot.
    """
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot
    return i + 1

# De-duplication Function
def deduplication(arr):
    """
    Removes duplicates from a sorted list of integers.
    Returns a new list with unique elements.
    """
    unique_elements = []
    for i in range(len(arr)):
        # Add unique elements to the new list
        if i == 0 or arr[i] != arr[i - 1]:
            unique_elements.append(arr[i])
    return unique_elements

# Main Function to Remove Duplicates
def remove_duplication(lst):
    """
    Sorts the list using Quick Sort and then removes duplicates.
    """
    # Quick Sort
    quick_sorting(lst, 0, len(lst) - 1)

    # De-duplication
    return deduplication(lst)

# Test Cases:
# 1. Handling null input: Should return an empty list.
# 2. Handling an array of length one: Should return the array itself.
# 3. Handling an array with all duplicates: Should return a single-element array.
# 4. Handling an array with all unique elements: Should return the array itself, sorted.

# Example Usage
LST = [50, 11, 33, 21, 40, 50, 40, 40, 21]
print(remove_duplication(LST))  # Expected output: [11, 21, 33, 40, 50]

