# Ashir Imran
# CSC 2720 Lab
# Date: 02/04/2024
def insertion_(arr):
    # Traverse through all elements starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # Store the current element to be compared
        j = i - 1  # Initialize a variable to traverse the sorted part of the array

        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at its correct position in the sorted array
        arr[j + 1] = key

    return arr  # Return the sorted array

# Test the function
test_arr = [50, 11, 33, 21, 40, 50, 40, 40, 21]
print("Original array:", test_arr)
sorted_arr = insertion_(test_arr)
print("Sorted array:", sorted_arr)
