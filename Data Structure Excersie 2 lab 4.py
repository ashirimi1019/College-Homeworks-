# Ashir Imran
# CSC 2720 Lab
# Date: 02/04/2024
def selection_(arr):
    # Iterate through each element in the array
    for i in range(len(arr)):
        min_idx = i  # Assume the current index is the minimum

        # Iterate through the unsorted part of the array to find the minimum element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update the minimum index if a smaller element is found

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr  # Return the sorted array

# Test the function
test_arr = [50, 11, 33, 21, 40, 50, 40, 40, 21]
print("Original array:", test_arr)
sorted_arr = selection_(test_arr)
print("Sorted array:", sorted_arr)
